# Write tests and implement the function using the following description:
# Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
    return str[:2]

def test_first_two():
    assert first_two('Hello') == 'He'
    assert first_two('X') == 'X'
    assert first_two('') == ''
    assert first_two('Hi') == 'Hi'
    assert first_two('He') == 'He'
    assert first_two('H') == 'H'
    assert first_two('Hii') == 'Hi'
    return('all g')

print(test_first_two())