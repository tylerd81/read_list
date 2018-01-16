#TODO: make an Item class instead of item all over the place
from readlist import ReadList

#format for database file
#title:author:total_pages:current_page:start_date:last_read

def main():
    read_list = ReadList()
    read_list.open('books.txt')

    for book_item in read_list:

        print('-*' * 20 + '-')
        read_list.display_item(book_item)
        print('-*' * 20 + '-')

        print(read_list.entry_to_line(book_item))

    add_new_item(read_list)
    read_list.save_data('books.txt')
#    read_list.dump_data()

def open_read_list(filename):
    pass

def display_read_list(read_list):
    pass

def add_new_item(read_list):
    d = {}
    d['title'] = input('Title: ')
    d['author'] = input('Author Name: ')
    d['total_pages'] = input('Number of Pages: ')
    d['current_page'] = input('Current Page: ')
    d['start_date'] = input('Start Date: ')
    d['last_read_date'] = input('Last Read Date: ')

    read_list.add_item(d)


if __name__ == '__main__':
    main()
