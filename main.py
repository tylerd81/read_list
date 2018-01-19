#TODO: make an Item class instead of item all over the place
from readlist import ReadList
from book import Book

#format for database file
#title:author:total_pages:current_page:start_date:last_read

def main():
    book_filename = 'books.txt'

    read_list = ReadList()
    read_list.open(book_filename)

    done = False

    while not done:
        selection = show_menu()

        if selection == '1':
            display_all_books(read_list)
        elif selection == '2':
            add_new_item(read_list)
        elif selection == '3':
            edit_selection(read_list)
        elif selection == '4':
            done = True
            read_list.save_data(book_filename)
        elif selection == '5':
            done = True

#    add_new_item(read_list)
#    read_list.save_data('books.txt')

def show_menu():
    menu = [
        '[ Choose an Option ]',
        '1) Display All Books',
        '2) Add A New Book',
        '3) Edit An Entry',
        '4) Quit',
        '5) Quit without saving',
    ]

    print('\n'.join(menu))

    choice = input('> ')

    return choice

def edit_selection(read_list):

    print('[ Choose an entry to edit: ]')
    idx = 1

    for book_item in read_list:
        print('{}: {}'.format(idx, book_item.title))
        idx += 1

    print('Type C To Cancel')
    selection = input('> ')

    if selection.lower() == 'c':
        return

    try:
        book_to_edit = read_list.get_book(int(selection) -1)
    except:
        print('Invalid Entry')
        return None

    if book_to_edit != None:
        edit_entry(read_list, book_to_edit)
    else:
        print('Entry not found')

def edit_entry(read_list, book_entry):

    print('*' * 20)
    print('Editing: {}'.format(book_entry.title))
    print('*' * 20)
    menu = [
        '1> Title',
        '2> Author',
        '3> Total Pages',
        '4> Current Page',
        '5> Start Date',
        '6> Last Read Date',
        '7> Display All Values',
        '8> Cancel',
        'D> DELETE',
    ]

    print('\n'.join(menu))
    field = input('Select field to edit> ')

    if field == 'D' or field == 'd':
        print('Removing Entry')
        read_list.remove(book_entry)
        print('Ok.')
        return

    if field == '7':
        read_list.display_item(book_entry)
        return

    val = input('Enter the new value: ')

    if field == '1':
        book_entry.set_title(val)
    elif field == '2':
        book_entry.set_author(val)
    elif field == '3':
        book_entry.set_total_pages(int(val))
    elif field == '4':
        book_entry.set_current_page(int(val))
    elif field == '5':
        book_entry.set_start_date(val)
    elif field == '6':
        book_entry.set_last_read_date(val)
    else:
        return

    print('Ok.')


def display_all_books(read_list):
    for book_item in read_list:
        print('-*'*20 + '-')
        read_list.display_item(book_item)
        print('-*'*20 + '-')

def add_new_item(read_list):

    title = input('Title: ')
    author = input('Author Name: ')
    total_pages = input('Number of Pages: ')
    current_page = input('Current Page: ')
    start_date = input('Start Date: ')
    last_read_date = input('Last Read Date: ')

    new_book = Book(title, author, total_pages, start_date)
    read_list.add_new_book(new_book)


if __name__ == '__main__':
    main()
