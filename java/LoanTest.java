

public class LoanTest extends UnitTestHarness {

    public static void main(String[] args) {

        LoanTest testController = new LoanTest();
        boolean showTestOutput = true;
        if ((args.length != 0) && (args[0].equals("hide")))
            showTestOutput = false;

        String testName;
        boolean testResult;
        
        {
            // test params
            testName = "Test 1";
            testResult = false;
            if (!showTestOutput)
                testController.hideConsoleOut();

            // specific test parameters
            Loan test1Loan = new Loan(100000,0,0.08,"years",25);

            // the test
            testResult = test1Loan.pmt() == 9367.88;

            // evaluate test
            testController.evaluateTest(testResult, testName, showTestOutput);

        } // end test

        {
            // test params
            testName = "Test 2";
            testResult = false;
            if (!showTestOutput)
                testController.hideConsoleOut();

            // specific test parameters
            Loan test1Loan = new Loan(100000,0,0.08,"months",25*12);

            // the test
            testResult = test1Loan.pmt() == 771.82;

            // evaluate test
            testController.evaluateTest(testResult, testName, showTestOutput);

        } // end test

        testController.printTestResults(testController.getClass().getSimpleName());

        if (testController.getScore() == 1.00) {
            System.out.println("Nice work! The test score is 1.00!");
            System.exit(0);
        } else {
            System.out.println("Aww shucks. There were some failures.");
            System.exit(1);
        }
        // return 42;

    }

};