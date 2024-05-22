word = input('Please enter a word :')
#print(word)
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in word :
    if char in vowels:
        vowel_count +=1
    
vowel_count = print(f'there are this many vowels : {vowel_count}')