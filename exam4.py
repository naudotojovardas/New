# Function: FizzBuzz
# Objective: Create a function `fizz_buzz` that evaluates the divisibility of a number by 3 and 5.
# If the number is divisible by 3, return "Fizz".
# If the number is divisible by 5, return "Buzz".
# If the number is divisible by both 3 and 5, return "FizzBuzz".
# Otherwise, return the number as a string.
# Parameters:
# - num: An integer to be evaluated.
# Returns:
# - A string based on the criteria above.


def fizz_buzz(N):
    N = 0
    for i in range(N):
        if i % 3 == 0 :
            print('Fizz')
        if i % 5 == 0 :
            print('Buzz')
        if i % 3 and i % 5 == 0 :
            print('Fizz_Buzz')
    else: 
        print('Nope u is kaka') #funny haha
        N += 1
        return N
N = float(input('input number: '))
print(fizz_buzz(N))

