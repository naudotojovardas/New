class factorial():

    def fac_try(n, fac_try):
        if n == 0:
            return 1
        else:
            return n * fac_try(n - 1)
        
    def test_factorial(factorial, fac_try): 
        for i in range(6):
            print(f'The factorial of {i} is {fac_try(i)}') 

    def test_factorial_1(factorial, fac_try):
        for i in range(6):
            print("Factorial of", i, "is", fac_try(i))

f = factorial()
f.test_factorial(f.fac_try)







