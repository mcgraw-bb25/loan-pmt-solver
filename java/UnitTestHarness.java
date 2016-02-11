/**
    @author: Matt McGraw
    Date: December 23, 2015
    Version: 1.0
*/

import java.util.ArrayList;
import java.io.PrintStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class UnitTestHarness {

    // initialize private variables
    private double testCounter = 0.0;
    private double testPassed = 0.0;
    private double testScore = 0.0;
    private String testOutput;

    // initialize the console as we will change print statements
    PrintStream console = System.out;
    ByteArrayOutputStream outputTest = new ByteArrayOutputStream();

    ArrayList<String> testNames = new ArrayList<String>();
    ArrayList<String> testResults = new ArrayList<String>();

    /**
        A short method to handle data processing for tests.
        Pass the test boolean value at the end of a test and the
        test data will be updated.

        Prints to output the result of the test.

        @params boolean testResult
        @params String testName
    */
    public void evaluateTest(boolean testResult, String testName, boolean textOutput) {
        
        if (testResult) {
            testNames.add(testName);
            testResults.add("Pass");
            this.testCounter++;
            this.testPassed++;
            if (textOutput)
                System.out.println(testName + ": Pass");
        }
        else {
            testNames.add(testName);
            testResults.add("Fail");
            this.testCounter++;
            if (textOutput)
                System.out.println(testName + ": Fail");
        }

    }

    /**
        Method to calculate and print the test results.
    */
    public void printTestResults(String testClass) {
        
        this.setConsoleOut();
        System.out.println();
        System.out.println("Testing Class: " + testClass);
        System.out.println("--Test Name-- \t\t --Result--");

        for (int i = 0; i < this.testNames.size(); i++) {
            System.out.println(testNames.get(i) +
                               "\t\t\t" + testResults.get(i));
        }

        this.testScore = (this.testPassed / this.testCounter) * 100;
        this.testOutput = String.format("Test Score: %1.2f%% - Passed %1.1f of %1.1f Tests",
                            testScore, testPassed, testCounter);
        System.out.println(testOutput);
        System.out.println();
        
    }

    /**
        Sets system output back to terminal.
    */
    public void setConsoleOut() {
        try {
                this.outputTest.flush();
                System.setOut(this.console); // resets the output to the console
        }
        catch (IOException error) {
                System.out.println("Error! Unable to flush output." + error);
        }        
    }

    /**
        Hides system output to outputTest
    */
    public void hideConsoleOu() {
        System.setOut(new PrintStream(this.outputTest));
    }

    public double getScore() {
        return this.testScore;
    }

} // end of UnitTestHarness