import time
from decimal import *


class LoanError(Exception):
    
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return __repr__(self.message)



class Loan(object):
    ''' 
    small class to compute solution to PMT on Loan
    construct new Loan giving:
        beginning_value > $0.00,
        future_value >= $0.00, (enter as $0 if fully repaying)
        interest_rate > 0.00, (annual interest rate, 0.05 for 5%)
            if periods are years, enter computed form 0.05
            if periods are months, enter computed form 0.05/12
            if periods are weeks, enter computed form 0.05/52
            if periods are days, computed form enter 0.05/365
        payment_frequency = ["years","months","weeks","days"]
        periods > 0, (enter number of periods)
    '''
    frequencies = {"years": 1, "months": 12, "weeks": 52, "days": 365}
    def __init__(self, beginning_value,
                       future_value,
                       interest_rate,
                       payment_frequency,
                       periods):
        self.beginning_value = beginning_value
        if payment_frequency in self.frequencies:
            self.interest_rate = interest_rate / self.frequencies[payment_frequency]
        else:
            raise LoanError("Incorrect payment frequency!")
        self.periods = periods
        self.future_value = future_value
        self.min_payment = (beginning_value - future_value) / periods
        self.recent_max = 0.0
        self.iterations = 0
        self.solved_payment = 0.0

    def pmt(self):
        ''' main api call to solve for a payment '''
        values = self.set_initial_values()
        self.solve(values)
        print ("Payment: %s\tTotal iterations: %s" % (self.solved_payment, self.iterations))
        return self.solved_payment

    def set_initial_values(self, payment=None):
        ''' compute beginning values for first period value '''
        if not payment:
            ''' set max payment '''
            payment = self.beginning_value * ((1 + self.interest_rate) ** self.periods)
        start_interest = self.beginning_value * self.interest_rate
        end_val = self.beginning_value - (payment - start_interest)
        values = [self.beginning_value, start_interest, payment, end_val]
        return values

    def solve(self, starting_values):
        ''' method implements solution to find payment '''
        self.iterations = self.iterations + 1
        this_payment = starting_values[2]
        loan_schedule = [starting_values]

        for i in range(0,self.periods):
            loan_schedule.append(self.next_period(i, loan_schedule[i]))

        if loan_schedule[self.periods-1][3] > 0.04 or loan_schedule[self.periods-1][3] < -0.04:
            if loan_schedule[self.periods-1][3] < 0.04:
                ''' ending balance negative, payment lower '''
                self.recent_max = this_payment
                next_payment = (this_payment + self.min_payment) / 2
                values = self.set_initial_values(next_payment)
                self.solve(values)
            elif loan_schedule[self.periods-1][3] > -0.04:
                ''' ending balance positive, payment higher '''
                next_payment = (this_payment + self.recent_max) / 2
                values = self.set_initial_values(next_payment)
                self.solve(values)
        else:
            solved_payment = Decimal(this_payment).quantize(Decimal('.01'), rounding=ROUND_UP)
            print ("Solution found! Periodic Payment: %s" % (solved_payment))
            self.solved_payment = float(solved_payment)
            return solved_payment

    def next_period(self, period, period_values):
        # beginning_value = Decimal(period_values[0]).quantize(Decimal('.01'), rounding=ROUND_UP)
        # interest_paid = Decimal(period_values[1]).quantize(Decimal('.01'), rounding=ROUND_UP)
        # payment = Decimal(period_values[2]).quantize(Decimal('.01'), rounding=ROUND_UP)
        # ending_value = Decimal(period_values[3]).quantize(Decimal('.01'), rounding=ROUND_UP)

        # print ("%s\t%s\t\t\t%s\t\t%s\t\t%s" % (period+1, beginning_value, interest_paid,
        #                                    payment, ending_value))


        next_period = [
            period_values[3],
            period_values[3] * self.interest_rate,
            period_values[2],
            period_values[3] - (period_values[2] - (period_values[3] * self.interest_rate))
        ]
        return next_period


if __name__ == "__main__":

    start = time.time()
    new_loan = Loan(100000,0,0.08,"years",25)
    a = new_loan.pmt()
    stop = time.time() - start
    print(stop)