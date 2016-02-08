import unittest
from pmt_solver import Loan

class TestPaymentSolver(unittest.TestCase):

    def test001(self):
        test_loan = Loan(100000,0,0.08,10)
        test_pmt = test_loan.pmt()
        self.assertEqual(test_pmt, 14902.95)
    
    def test002(self):
        test_loan = Loan(100000,0,0.07,10)
        test_pmt = test_loan.pmt()
        self.assertEqual(test_pmt, 14237.75)
    
    def test003(self):
        test_loan = Loan(100000,0,0.06,10)
        test_pmt = test_loan.pmt()
        self.assertEqual(test_pmt, 13586.80)


if __name__ == "__main__":
    unittest.main()