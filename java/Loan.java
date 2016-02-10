
import javax.json.*;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

enum Frequencies { 

    YEARS(1.0), MONTHS(12.0), WEEKS(52.0), DAYS(365.0);
    
    private double multiplier;

    private Frequencies(double multiplier) {
        this.multiplier = multiplier;
    }

    public double getMultiplier() {
        return multiplier;
    }

};

public class Loan {

    private double beginningValue, futureValue, interestRate;
    private String paymentFrequency;
    private int periods;
    static Frequencies paymentFreq;
    
    public Loan (double beginningValue, double futureValue,
                double interestRate, String paymentFrequency,
                int periods) {
        // System.out.println(); 
        this.beginningValue = beginningValue;
        this.futureValue = futureValue;
        this.interestRate = interestRate / paymentFreq.valueOf(paymentFrequency.toUpperCase()).getMultiplier();
        this.paymentFrequency = paymentFrequency;
        this.periods = periods;
    }

    public double pmt() {
        @SuppressWarnings("unchecked")
        Map<String,Double> firstRow = this.setInitialValues();
        System.out.println(firstRow);
        return 9367.88;
    }

    /**
        Override method to allow for optional payment.
        Payment should be a double to run through next solver.
        Default = 0.0
        @params double payment, optional
        @returns Map of first row of values
    */
    private Map setInitialValues() {
        @SuppressWarnings("unchecked")
        Map<String, Double> initialValues = this.setInitialValues(0.0);
        return initialValues;
    }

    private Map setInitialValues(double payment) {
        Map<String, Double> initialValues = new HashMap<String, Double>();
        double beginning_value, interest_paid, ending_value;
        beginning_value = this.beginningValue;
        interest_paid = beginning_value * this.interestRate;
        ending_value = beginning_value - (payment - interest_paid);
        initialValues.put("beginning_value", beginning_value);
        initialValues.put("interest_paid", interest_paid);
        initialValues.put("payment", payment);
        initialValues.put("ending_value", ending_value);
        return initialValues;
    }
    
}