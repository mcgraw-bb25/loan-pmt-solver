require "minitest/autorun"
# requite "pmt_solver"

class TestPaymentSolver < MiniTest::Unit::TestCase
    def setup
        @loan = Loan.new(100000,0,0.08,"years",25)
    end

    def test_loan_one
        assert_equal 9367.88, @loan.pmt
    end

end
