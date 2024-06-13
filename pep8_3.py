def Greet_User (age):
    age_verify = age > 21
    
    if age_verify == True:
        print("Welcome")
    if age_verify == False:
        print("Access denied")

Greet_User(22)