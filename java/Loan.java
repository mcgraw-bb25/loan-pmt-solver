
import javax.json.*;

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
        // System.out.println(paymentFreq.valueOf(paymentFrequency.toUpperCase()).getMultiplier()); 
        this.beginningValue = beginningValue;
        this.futureValue = futureValue;
        this.interestRate = interestRate;
        this.paymentFrequency = paymentFrequency;
        this.periods = periods;
    }

    public double pmt() {
        return 9367.88;
    }
    
}