class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book_title):
        self.book_list.append(book_title)
        print(f'Книга "{book_title}" добавлена в библиотеку.')

    def remove_book(self, book_title):
        if book_title in self.book_list:
            self.book_list.remove(book_title)
            print(f'Книга "{book_title}" удалена из библиотеки.')
        else:
            print(f'Книги "{book_title}" нет в библиотеке.')

    def find_book(self, book_title):
        if book_title in self.book_list:
            print(f'Книга "{book_title}" найдена в библиотеке.')
        else:
            print(f'Книги "{book_title}" нет в библиотеке.')

library = Library()
library.add_book("Шерлок Холмс. Все повести и рассказы о сыщике")
library.add_book("Прислуга")
library.add_book("Моя вина")

library.find_book("Прислуга")
library.find_book("Отцы и дети")

library.remove_book("Моя вина")
library.remove_book("Дубровский")
