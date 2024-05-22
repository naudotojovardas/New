name = input("Enter your name please: ")
surname = input("Enter your surname please: ")
age = float(input("Enter your age please: "))
legal_age = 21

if  age < legal_age :
    print(f"Sorry, " + name.upper() + " you are too young ! :( ")
elif age > legal_age :
    print(f"Welcome {name.upper()[0]}, have a great evening!")
elif age == legal_age :
    print(f"Welcome {name.upper()[0]}, have a great evening!")
    