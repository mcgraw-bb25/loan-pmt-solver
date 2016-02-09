require "time"

class Loan
    attr_reader :beginning_value, :future_value, 
                :interest_rate, :payment_frequency, :periods

    def initialize(args)
        @beginning_value = args[:beginning_value]
        @future_value = args[:future_value]
        ## test for invalid frequency later
        @interest_rate = args[:interest_rate] / frequencies(args[:payment_frequency])
        @payment_frequency = args[:payment_frequency]
        @periods = args[:periods]
        @min_payment = (beginning_value - future_value) / periods
        @recent_max = 0.0
        @iterations = 0
        @solved_payment = 0.0
    end

    def set_initial_values(payment=nil)
        values = Hash.new
        if payment.nil?
            payment = beginning_value * ((1 + interest_rate) ** periods)
        end
        values[:beginning_value] = beginning_value
        values[:interest_paid] = beginning_value * interest_rate
        values[:payment] = payment
        values[:ending_value] = beginning_value - (payment - values[:interest_paid])
        return values
    end

    def frequencies(frequency)
        frequencies = Hash.new
        frequencies = {"years" => 1,
                       "months" => 12,
                       "weeks" => 52,
                       "days" => 365}
        frequencies.fetch(frequency)
    end

    def pmt
        9367.88
    end
end

if __FILE__ == $0
    loops = 20
    total_time = 0.0
    # actual = "Goodbye"
    loops.times do
        t = Time.new.to_f
        # actual = run_file()
        runtime = Time.new.to_f - t
        # puts "#{t}"
        total_time = total_time + runtime
    end
    # runtime = total_time / loops
    # puts "Lang:Ruby,Result:#{actual},Runtime:#{runtime}"
    values = {  "beginning_value": 100000,
                "future_value": 0,
                "interest_rate": 0.08,
                "payment_frequency": "years",
                "periods": 25}
    loan = Loan.new(values)
    puts loan.frequencies("months")
    puts loan.beginning_value
    puts loan.set_initial_values()
    puts loan.set_initial_values(500)
end

