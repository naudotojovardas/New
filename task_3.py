def equation(a,b):
    try:
        plus = a + b
        minus = a - b
        divide = a / b
        multiply = a * b
    except TypeError as e:
        return "error"
    return (plus, minus, divide, multiply)

a = float(input("Enter number 1: "))  
b = float(input("Enter number 2: "))  

print(equation(a,b))