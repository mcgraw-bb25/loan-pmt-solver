require "time"

class Loan
    attr_reader :beginning_value, :future_value, 
                :interest_rate, :payment_frequency, :periods,
                :solved_payment, :min_payment, :recent_max, :iterations

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
        values[:beginning_value] = beginning_value.to_f
        values[:interest_paid] = (beginning_value * interest_rate).to_f
        values[:payment] = payment.to_f
        values[:ending_value] = (beginning_value - (payment - values[:interest_paid])).to_f
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
        values = []
        starting_value = set_initial_values()
        values << starting_value
        solve(values)
        return solved_payment
    end

    def solve(values)
        @iterations = iterations + 1
        current_payment = values[0][:payment]

        period = 0
        (periods-1).times do
            values << next_period(values[period])
            period = period + 1
        end
        
        if values[-1][:ending_value] > 0.04 or values[-1][:ending_value] < -0.04
            
            # puts "payment #{values[-1][:payment]} ending #{values[-1][:ending_value]}"
            if values[-1][:ending_value] < 0.04
                ## ending balance negative payment smaller
                @recent_max = current_payment
                # puts "recent max now #{recent_max}"
                next_payment = ((current_payment + min_payment) / 2).to_f
                next_values = []
                starting_value = set_initial_values(next_payment)
                next_values << starting_value
                solve(next_values)
            elsif values[-1][:ending_value] > -0.04
                ## ending balance positive, payment bigger
                next_payment = ((current_payment + recent_max) / 2).to_f
                next_values = []
                starting_value = set_initial_values(next_payment)
                next_values << starting_value
                solve(next_values)
            end
        else
            @solved_payment = current_payment.to_f.round(2)
        end
    end

    def next_period(values)
        next_values = {}
        next_values[:beginning_value] = values[:ending_value].to_f
        next_values[:interest_paid] = (next_values[:beginning_value] * interest_rate).to_f
        next_values[:payment] = values[:payment]
        next_values[:ending_value] = (next_values[:beginning_value] - (values[:payment] - next_values[:interest_paid])).to_f
        return next_values
    end
end

if __FILE__ == $0

    loan_book = []
    loan_book << Loan.new({ "beginning_value": 100000,
                            "future_value": 0,
                            "interest_rate": 0.08,
                            "payment_frequency": "years",
                            "periods": 25})
    loan_book << Loan.new({ "beginning_value": 100000,
                            "future_value": 0,
                            "interest_rate": 0.08,
                            "payment_frequency": "months",
                            "periods": 25*12})
    loan_book << Loan.new({ "beginning_value": 100000,
                            "future_value": 0,
                            "interest_rate": 0.08,
                            "payment_frequency": "weeks",
                            "periods": 25*52})
    loan_book << Loan.new({ "beginning_value": 100000,
                            "future_value": 0,
                            "interest_rate": 0.08,
                            "payment_frequency": "days",
                            "periods": 25*365})

    times = Hash.new
    loan_book.each do |loan|
        # puts loan.pmt
        total_time = 0.0
        payment = 0.0
        loops = 20
        loops.times do
            t = Time.new.to_f
            pmt = loan.pmt
            runtime = Time.new.to_f - t
            total_time = total_time + runtime
            payment = pmt
        end
        runtime = total_time / loops
        pmt_info = Hash.new
        pmt_info[:payment] = payment
        pmt_info[:runtime] = runtime
        times[loan.payment_frequency] = pmt_info
    end

    puts times
        
end

