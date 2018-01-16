class ReadList():

    NUM_OF_FIELDS = 6

    def __init__(self):
        self.separator = ':'
        self.read_data = []

    def open(self, filename):
        with open(filename) as read_list_file:
            for line in read_list_file:
                if line.strip() != '':
                    self.add_item(self.line_to_entry(line))

    def add_item(self, item):
        if item == None or len(item.keys()) != ReadList.NUM_OF_FIELDS:
            return None

        self.read_data.append(item)
        return item

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

    def dump_data(self):
        for book_item in self.read_data:
            self.display_item(book_item)
