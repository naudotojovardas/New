# Create a class method to return the list of prime numbers up to a given number.

class Prime:
    @classmethod
    def get_primes(cls, n):
        primes = []
        for i in range(2, n+1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        return primes
    
print(Prime.get_primes(100))
print(Prime.get_primes(1000))