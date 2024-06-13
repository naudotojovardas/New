class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_title(self):
        return "Title: " + self.title
    
    def get_author(self):
        return "Author: " + self.author

pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen")
hamlet = Book("Hamlet", "William Shakespeare")
war_and_peace = Book("War and Peace", "Leo Tolstoy")

print(pride_and_prejudice.get_title()) 
print(pride_and_prejudice.get_author()) 

print(hamlet.get_title()) 
print(hamlet.get_author())

print(war_and_peace.get_title())
print(war_and_peace.get_author())
