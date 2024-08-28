# Write tests and implement the function using the following description:
# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def sorta_sum(a, b):
    if 10 <= a + b <= 19 or 11<= a + b <=18 or 12<= a + b <=17 or 13<= a + b <=16 or 14<= a + b <=15:
        return 20
    else:
        return a + b
    
def tets():
    assert sorta_sum(3, 4) == 7
    assert sorta_sum(9, 4) == 20
    assert sorta_sum(10, 11) == 21
    assert sorta_sum(12, -2) == 20
    assert sorta_sum(12, 3) == 20
    assert sorta_sum(10, 9) == 20
    return('all a okey;)')

print(tets())