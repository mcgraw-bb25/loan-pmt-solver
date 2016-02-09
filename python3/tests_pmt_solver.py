import unittest
from pmt_solver import Loan

class TestPaymentSolver(unittest.TestCase):

    def test001(self):
        ''' years '''
        test_loan = Loan(100000,0,0.08,"years",25)
        test_pmt = test_loan.pmt()
        self.assertEqual(test_pmt, 9367.88)
    
    def test002(self):
        ''' months '''
        test_loan = Loan(100000,0,0.08,"months",25*12)
        test_pmt = test_loan.pmt()
        self.assertEqual(test_pmt, 771.82)
    
    def test003(self):
        ''' weeks '''
        test_loan = Loan(100000,0,0.08,"weeks",25*52)
        test_pmt = test_loan.pmt()
        self.assertEqual(test_pmt, 177.97)

    def test004(self):
        ''' days '''
        test_loan = Loan(100000,0,0.08,"days",25*365)
        test_pmt = test_loan.pmt()
        self.assertEqual(test_pmt, 25.35)

if __name__ == "__main__":
    unittest.main()