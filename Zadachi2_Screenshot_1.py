class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
book1 = Book("Война и мир", "Лев Толстой")
print(book1.get_title())
print(book1.get_title())