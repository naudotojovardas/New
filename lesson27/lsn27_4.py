#create a lambda function to extract the year, month, day, and time from a given datetime object and print each component.
#lets wrap our print commands with a function that will print the output in a more readable way.

class cosmetic:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('----------------')
        self.func()
        print('----------------')

import datetime as dt 

@cosmetic
def full_date():
    now = dt.datetime.now()
    print(f'Full date and time: ', now)

def year():
    year = lambda x: x.year
    return year

def month():
    month = lambda x: x.month
    return month

def day():  
    day = lambda x: x.day
    return day

def time():
    time = lambda x: x.time()
    return time

@cosmetic
def print_date():
    now = dt.datetime.now()
    print(f'Year: {year()(now)}')
    print(f'Month: {month()(now)}')
    print(f'Day: {day()(now)}')
    print(f'Time: {time()(now)}')

print_date()
full_date()
