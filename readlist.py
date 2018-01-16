import math

class ReadList():

    NUM_OF_FIELDS = 6

    def __init__(self):
        self.separator = ':'
        self.read_data = []
        self.current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_item < len(self.read_data):
            data = self.read_data[self.current_item]
            self.current_item += 1
            return data
        else:
            raise StopIteration

    def open(self, filename):
        with open(filename) as read_list_file:
            for line in read_list_file:
                line = line.strip()
                if line != '':
                    self.add_item(self.line_to_entry(line))

    def save_data(self, filename):

        with open(filename, 'w') as file:
            for book_item in self.read_data:
                line = self.entry_to_line(book_item)
                file.write(line + '\n')

    def add_item(self, item):
        if item == None or len(item.keys()) != ReadList.NUM_OF_FIELDS:
            return None

        self.read_data.append(item)
        return item

    def entry_to_line(self, item):
        line = []
        line.append(item['title'])
        line.append(item['author'])
        line.append(item['total_pages'])
        line.append(item['current_page'])
        line.append(item['start_date'])
        line.append(item['last_read_date'])

        return '{}'.format(self.separator).join(line)

    def line_to_entry(self, line):
        #format is:
        #title:author:total_pages:current_page:start_date:last_read_date

        if line[0] == '#':
            return None # comment

        data = line.split(self.separator)

        if len(data) != ReadList.NUM_OF_FIELDS:
            print('Error in database file:\n{}'.format(line))
            return None


        return {
            'title' : data[0],
            'author': data[1],
            'total_pages' : data[2],
            'current_page' : data[3],
            'start_date' : data[4],
            'last_read_date' : data[5],
        }

    def display_item(self, item):

        print('Title: ' + item['title'].title())
        print('Author: ' + item['author'].title())
        print('Pages: ' + item['total_pages'])
        print('Current Page: ' + item['current_page'])
        print('Start Date: ' + item['start_date'])
        print('Last Read: ' + item['last_read_date'])
        print('Status: ' + self.calculate_percent_read(item))

    def calculate_percent_read(self, item):
        total_pages = int(item['total_pages'])
        pages_read = int(item['current_page'])

        percent_read = math.floor((pages_read / total_pages) * 100)

        return '{}% Finished.'.format(percent_read)

    def dump_data(self):
        for book_item in self.read_data:
            self.display_item(book_item)
