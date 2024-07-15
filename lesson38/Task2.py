# Write a function that converts a given date from the format dd.mm.yyyy to yyyy mm dd.
#  Don't worry about the logic of the dates; treat this purely as a text manipulation task. 

def convert_date(date):
    date = date.split('.')
    return f'{date[2]}.{date[1]}.{date[0]}'

print(convert_date('01.12.2020')) 