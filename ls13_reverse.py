word = input('word: ')

def reverse_string(word):
    reverse = word[::-1]
    return reverse

def capitalize_string(word):
    capital = word.capitalize()
    return capital

def count_characters(word):
    counted = len(word)
    return counted

print(reverse_string(word))


