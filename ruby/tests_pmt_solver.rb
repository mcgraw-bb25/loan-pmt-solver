require "minitest/autorun"
require_relative "pmt_solver"

class TestPaymentSolver < MiniTest::Unit::TestCase
    def setup
        values = {  "beginning_value": 100000,
                    "future_value": 0,
                    "interest_rate": 0.08,
                    "payment_frequency": "years",
                    "periods": 25}
        @loan = Loan.new(values)
    end

    def test_loan_one
        assert_equal 9367.88, @loan.pmt
    end

end

