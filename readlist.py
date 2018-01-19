import math
from book import Book

class ReadList():

    NUM_OF_FIELDS = 6

    def __init__(self):
       self.separator = ':'
       self.book_list = []
       self.current_book = 0

    def __iter__(self):
        return self

    # Iterator next()
    def __next__(self):
        if self.current_book < len(self.book_list):
            next_book = self.book_list[self.current_book]
            self.current_book += 1
            return next_book
        else:
            raise StopIteration

    # open() opens the saved reading list file and adds each book to the
    # book_list
    def open(self, filename):
        with open(filename) as read_list_file:
            for line in read_list_file:
                line = line.strip()
                if line != '':
                    self.book_list.append(Book(save_string=line))

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for book_item in self.book_list:
                line = book_item.to_save_string()
                file.write(line + '\n')


    def add_new_book(self, book_item):
        self.book_list.append(book_item)

    def display_item(self, item):

        print('Title: ' + item.title)
        print('Author: ' + item.author)
        print('Pages: ' + str(item.total_pages))
        print('Current Page: ' + str(item.current_page))
        print('Start Date: ' + item.start_date)
        print('Last Read: ' + item.last_read_date)
        print('Status: ' + str(item.get_percent_read()))
