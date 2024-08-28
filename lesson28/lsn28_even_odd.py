# Use Lambda to count even and odd numbers in a given array.

def count_even_odd(arr):
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

Arr = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original array:", Arr)
even, odd = count_even_odd(Arr)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)
