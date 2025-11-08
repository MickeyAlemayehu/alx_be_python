principal = 1000
rate = 0.05
time = 3
def simple_interest(principal, rate, time):
    interest = principal * rate * time
    return interest


print("The simple interest is:",simple_interest(principal, rate, time))