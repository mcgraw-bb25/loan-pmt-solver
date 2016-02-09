require "minitest/autorun"
require_relative "pmt_solver"

class TestPaymentSolver < MiniTest::Unit::TestCase
    # def setup
    #     values = {  "beginning_value": 100000,
    #                 "future_value": 0,
    #                 "interest_rate": 0.08,
    #                 "payment_frequency": "years",
    #                 "periods": 25}
    #     @loan = Loan.new(values)
    # end

    def test_loan_one
        values = {  "beginning_value": 100000,
                    "future_value": 0,
                    "interest_rate": 0.08,
                    "payment_frequency": "years",
                    "periods": 25}
        loan1 = Loan.new(values)
        assert_equal 9367.88, loan1.pmt
    end

    def test_loan_two
        values = {  "beginning_value": 100000,
                    "future_value": 0,
                    "interest_rate": 0.08,
                    "payment_frequency": "months",
                    "periods": 25}
        loan2 = Loan.new(values)
        assert_equal 771.82, loan2.pmt
    end

end

