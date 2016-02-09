require "minitest/autorun"
require_relative "pmt_solver"

class TestPaymentSolver < MiniTest::Unit::TestCase

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
                    "periods": 25*12}
        loan2 = Loan.new(values)
        assert_equal 771.82, loan2.pmt
    end

    def test_loan_three
        values = {  "beginning_value": 100000,
                    "future_value": 0,
                    "interest_rate": 0.08,
                    "payment_frequency": "weeks",
                    "periods": 25*52}
        loan3 = Loan.new(values)
        assert_equal 177.97, loan3.pmt
    end

    def test_loan_four
        values = {  "beginning_value": 100000,
                    "future_value": 0,
                    "interest_rate": 0.08,
                    "payment_frequency": "days",
                    "periods": 25*365}
        loan4 = Loan.new(values)
        assert_equal 25.35, loan4.pmt
    end

end

