def calculator():
    try:
        outcome = (a / b) 
        return outcome
    except (UnboundLocalError, TypeError):
        print('oops')
        return None


a = float(input('nr?: '))
b = float(input('nr?: '))

print(calculator())

# try: 
#     except FloatingPointError
# print('oops')

# print(calculator())
    
