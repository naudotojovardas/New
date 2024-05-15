num1 = float(input("Enter number 1 :"))
thing = (input("enter thing +,-,*,/ :"))
num2 = float(input("enter number 2 :"))
result =""

if thing == "+" :
    result = num1 + num2
elif thing == "-" : 
    result = num1 - num2
elif thing == "*" :
    result = num1 * num2
elif thing == "/" :
    result = num1 / num2
print(f"result of {num1} {thing} {num2} is {result}")