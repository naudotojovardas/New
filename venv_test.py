# source venv/Source/activate
from random_word import RandomWords

r = RandomWords()

words = r.get_random_words(count=5)
capitalized_words = [w.upper() for w in words]
sorted_words = sorted(capitalized_words)

for word in sorted_words:
    print(word)

# from random_word import RandomWords
 
# r = RandomWords()
 
# word = r.get_random_word()
# print("Random word:", word)