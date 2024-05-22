num1 = int(input('Input a number between 1 and 10 :'))
num2 = int(input('Input a number between 1 and 10 :'))

count = 0
for i in range(num1, num2 +1):
    if i % 2 == 0 : 
        count += i 

print(count)
