import math
# TODO 1: Place your code for `pretty_print_int` here
def pretty_print_int(number):
    
    return str(f"{number:,}")


# TODO 2: Place your code for `pretty_print_dollars` here
def pretty_print_dollars(number):
    if number < 0:
         number = abs(number)
         return str(f"-${number:,.2f}")
    else:
        return str(f"${number:,.2f}")    

    

# TODO 3: Place your code for `make_field` here
def make_field(content,length):
    content = str(content)
    if len(content) <= (length - 2):
        empty = length - len(content) - 1
        spaces = " " * empty
        return "|" + spaces + content + " |"

    else:
        content = content[:length - 2]
        empty = length - len(content) - 1
        spaces = " " * empty
        return "|" + spaces + content + " |"
  

# TODO 4: Place your code for `make_line` here
def make_line(length):

    line_length = length * "-"

    return '+' + str(line_length) + '+'


# TODO 5: Place your code for `simulate_infection` here
def simulate_infection(population, initial_infected, r_number):
    infected = initial_infected
    deceased = 0
    day = 1
    
    while population >= 0:
        population = population - deceased
        print(day, max(0, population))
        deceased = infected
        infected = math.ceil(infected * r_number)
        day += 1
         
        

# TODO 6: Place your code for `compound_interest` here
def compound_interest(init_principal, acc_rate, acc_cmp_freq, years):
    
    if acc_cmp_freq != 0:
        final_amount = init_principal * (1 + (acc_rate / acc_cmp_freq)) ** (acc_cmp_freq * years)
        
        return final_amount
    else:
        acc_comp_freq = 0
        final_amount = init_principal * math.e **(acc_rate * years)

        return final_amount

# TODO 7: Place your code for `simulate_account_balance` here
def simulate_account_balance(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    init_balance = init_principal - setup_fee

    for year in range(2,years + 1,2):
        new_balance = round(compound_interest(init_balance, acc_rate, acc_cmp_freq, year) , 2)
        print(year, new_balance)


# TODO 8: Place your code for `simulate_infection_pp` here
def simulate_infection_pp(population, initial_infected, r_number):
    print(make_line(5) + make_line(12))
    print(make_field("Day", 5) + make_field("Population", 12))
    print(make_line(5) + make_line(12))

    infected = initial_infected
    deceased = 0

    day = 1

    print(make_field(str(day), 5) + make_field(pretty_print_int(population), 12))

    while population != 0:
        deceased = deceased + infected
        population -= infected

        if population < 0:
            population = 0

        infected = math.ceil(infected * r_number)
        day += 1

        print(make_field(str(day), 5) + make_field(pretty_print_int(population), 12))
    print(make_line(5) + make_line(12))



# TODO 9: Place your code for `simulate_account_balance_pp` here
def simulate_account_balance_pp(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    
    #Get total length including commas and dollars signs
    total_years = 2
    for i in range(int((years / 2))):
        amount = round(compound_interest(init_principal - setup_fee, acc_rate, acc_cmp_freq, total_years), 2)        
        total_years += 2
    x =  len("${:0,.2f}".format(amount)) + 2   
    #-------------------------------------------------------------------------------------------------------- 
    
    print(make_line(6) + make_line(x))
    print(make_field("Year", 6) + make_field("Balance", x))
    print(make_line(6) + make_line(x))
    total_years = 2
    for i in range(int((years / 2))):
        amount = round(compound_interest(init_principal - setup_fee, acc_rate, acc_cmp_freq, total_years), 2)        
        print(make_field(str(total_years), 6) + make_field(pretty_print_dollars(amount), x))          
        total_years += 2
    print(make_line(6) + make_line(x))
    
   
if __name__ == '__main__':
    pass # use this block for validation
    simulate_account_balance_pp(100000.00, 0.02, 0, 13, 10)


