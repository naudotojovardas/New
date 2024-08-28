# Write tests and implement the function using the following description:
# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

def left2(str):
    return str[2:] + str[:2]

def test():
    assert left2('Hello') == 'lloHe'
    assert left2('java') == 'vaja'
    assert left2('Hi') == 'Hi'
    assert left2('code') == 'deco'
    assert left2('cat') == 'tca'
    assert left2('12345') == '34512'
    assert left2('Chocolate') == 'ocolateCh'
    assert left2('bricks') == 'icksbr'
    assert left2('apple') == 'pleap'
    assert left2('carrot') == 'rrotca'
    assert left2('abc') == 'cab'
    assert left2('ab') == 'ab'
    assert left2('a') == 'a'
    assert left2('') == ''
    return('All g')

print(test())