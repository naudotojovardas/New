def is_magic_number(n):

    def sum_of_digits(num):
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total

    while n >= 10:
        n = sum_of_digits(n)

    return n == 1

print(is_magic_number(50113))  
print(is_magic_number(1234)) 
print(is_magic_number(12345))
