from readlist import ReadList

def main():
    read_list = ReadList()
    read_list.open('books.txt')

    for book_item in read_list:

        print('-*' * 20 + '-')
        read_list.display_item(book_item)
        print('-*' * 20 + '-')

        print(read_list.entry_to_line(book_item))

#    read_list.dump_data()

def open_read_list(filename):
    pass

def display_read_list(read_list):
    pass

def add_new_item(read_list):
    pass

if __name__ == '__main__':
    main()
