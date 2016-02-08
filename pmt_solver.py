




class Loan(object):

    def __init__(self, beginning_value,
                       future_value,
                       interest_rate,
                       periods):
        self.beginning_value = beginning_value
        self.interest_rate = interest_rate
        self.periods = periods
        self.future_value = future_value
        self.initial_guess = (self.beginning_value / self.periods) * (1 + self.interest_rate) * 1.5

    def pmt(self):

        print ("Period\tBeginning Value\t\tInterest\tPayment\t\tEnding")
        values = self.set_initial_values()
        self.solve(values)

    def set_initial_values(self, payment=None):
        if not payment:
            payment = self.initial_guess
        start_val = self.beginning_value
        start_interest = self.beginning_value * self.interest_rate
        pmt = payment
        end_val = start_val - (payment - start_interest)

        values = [start_val, start_interest, payment, end_val]

        return values

    def solve(self, starting_values):
        this_pmt = starting_values[2]
        loan_schedule = [starting_values]

        # iteration_values = starting_values
        for i in range(0,self.periods):
            loan_schedule.append(self.next_period(i, loan_schedule[i]))

        if len(loan_schedule) == self.periods:
            print ("Periods correct")
        
        if loan_schedule[self.periods-1][3] < 1 and loan_schedule[self.periods-1][3] > -1:
            print ("Solution found! Periodic Payment: %s" % (loan_schedule[2]))
        else:
            if loan_schedule[self.periods-1][3] < 1:
                ''' ending balance negative, pmt lower '''
                next_pmt = this_pmt / 2
                values = self.set_initial_values(next_pmt)
                self.solve(values)
            else:
                ''' ending balance positive, pmt higher '''
                next_pmt = this_pmt * 2
                values = self.set_initial_values(next_pmt)
                self.solve(values)


    def next_period(self, period, period_values):
        print ("%s\t%s\t\t\t%s\t\t%s\t\t%s" % (period+1, period_values[0], period_values[1],
                                           period_values[2], period_values[3]))
        next_period = [
            period_values[3],
            period_values[3] * self.interest_rate,
            period_values[2],
            period_values[3] - (period_values[2] - (period_values[3] * self.interest_rate))
        ]
        return next_period


if __name__ == "__main__":

    new_loan = Loan(100000,0,0.06,10)
    new_loan.pmt()