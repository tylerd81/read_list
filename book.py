# Format for the data is:
# title:author:total_pages:current_page:start_date:last_read_date

import math

class Book():

    NUM_OF_FIELDS = 6

    def __init__(
        self,
        title='',
        author='',
        total_pages='',
        start_date='',
        current_page=0,
        last_read_date='',
        save_string=None):

        self.separator = ':'

        if not save_string:
            self.create_book(title, author, total_pages, start_date,
                             current_page, last_read_date)
        else:
            self.create_book_from_string(save_string)

    def create_book(self, title, author, total_pages, start_date, current_page,
                   last_read_date):

        self.set_title(title)
        self.set_author(author)
        self.set_total_pages(total_pages)
        self.set_start_date(start_date)

        self.set_current_page(current_page)

        if last_read_date == '':
            self.set_last_read_date(start_date)
        else:
            self.set_last_read_date(last_read_date)

    def create_book_from_string(self, line):
        if line[0] == '#':
            return None

        data = line.split(self.separator)
        if len(data) != Book.NUM_OF_FIELDS:
            print('Error in database file:\n{}'.format(data))
            return None

        title = data[0]
        author = data[1]
        total_pages = data[2]
        current_page = data[3]
        start_date = data[4]
        last_read_date = data[5]

        self.create_book(title, author, total_pages, start_date, current_page,
                         last_read_date)

        return self

    def set_current_page(self, pages_read):
        self.current_page = int(pages_read)

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_total_pages(self, total_pages):
        self.total_pages = int(total_pages)

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_last_read_date(self, last_read_date):
        self.last_read_date = last_read_date

    def get_percent_read(self):
        if self.current_page == 0:
            print('No pages read.')
            return 0

        percent_read = math.floor((self.current_page / self.total_pages) * 100)
        return percent_read

    def to_save_string(self):
        line = []
        line.append(self.title)
        line.append(self.author)
        line.append(str(self.total_pages))
        line.append(str(self.current_page))
        line.append(self.start_date)
        line.append(self.last_read_date)

        return self.separator.join(line)


