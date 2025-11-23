from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print ("Current date and time: ", current_date)
    return current_date
    


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: ")) 
    current_date = display_current_datetime()
    future_date = current_date + timedelta(days=number_of_days) 
    print ("Future date: ", future_date.date())

calculate_future_date()