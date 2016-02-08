import time
from decimal import *




class Loan(object):

    def __init__(self, beginning_value,
                       future_value,
                       interest_rate,
                       periods):
        self.beginning_value = beginning_value
        self.interest_rate = interest_rate
        self.periods = periods
        self.future_value = future_value
        # self.initial_guess = (self.beginning_value / self.periods) * (1 + self.interest_rate) * 1.5
        self.min_payment = (beginning_value - future_value) / periods
        self.max_payment = beginning_value * ((1 + interest_rate) ** periods)
        self.recent_max = 0.0
        self.iterations = 0
        self.payment_history = []
        self.solved_payment = 0.0

    def pmt(self):
        ''' main api call to solve for a payment '''
        # print ("Period\tBeginning Value\t\tInterest\tPayment\t\tEnding")
        values = self.set_initial_values()
        self.solve(values)
        print ("Payment: %s\tTotal iterations: %s" % (self.solved_payment, self.iterations))
        return self.solved_payment

    def set_initial_values(self, payment=None):
        if not payment:
            payment = self.max_payment
        start_val = self.beginning_value
        start_interest = self.beginning_value * self.interest_rate
        pmt = payment
        end_val = start_val - (payment - start_interest)

        values = [start_val, start_interest, payment, end_val]

        return values

    def solve(self, starting_values):
        self.iterations = self.iterations + 1
        this_pmt = starting_values[2]
        self.payment_history.append(this_pmt)
        loan_schedule = [starting_values]

        # iteration_values = starting_values
        for i in range(0,self.periods):
            loan_schedule.append(self.next_period(i, loan_schedule[i]))

        if len(loan_schedule) == self.periods:
            print ("Periods correct")

        if loan_schedule[self.periods-1][3] > 0.04 or loan_schedule[self.periods-1][3] < -0.04:
            if loan_schedule[self.periods-1][3] < 0.04:
                ''' ending balance negative, pmt lower '''
                self.recent_max = this_pmt ## can use this as anchor
                next_pmt = (this_pmt + self.min_payment) / 2
                values = self.set_initial_values(next_pmt)
                self.solve(values)
            elif loan_schedule[self.periods-1][3] > -0.04:
                ''' ending balance positive, pmt higher '''
                next_pmt = (this_pmt + self.recent_max) / 2
                values = self.set_initial_values(next_pmt)
                self.solve(values)
        else:
            solved_payment = Decimal(this_pmt).quantize(Decimal('.01'), rounding=ROUND_UP)
            print ("Solution found! Periodic Payment: %s" % (solved_payment))
            self.solved_payment = float(solved_payment)
            return solved_payment

    def next_period(self, period, period_values):
        beginning_value = Decimal(period_values[0]).quantize(Decimal('.01'), rounding=ROUND_UP)
        interest_paid = Decimal(period_values[1]).quantize(Decimal('.01'), rounding=ROUND_UP)
        payment = Decimal(period_values[2]).quantize(Decimal('.01'), rounding=ROUND_UP)
        ending_value = Decimal(period_values[3]).quantize(Decimal('.01'), rounding=ROUND_UP)
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
    new_loan = Loan(100000,0,0.08,10)
    a = new_loan.pmt()
    stop = time.time() - start
    print(stop)