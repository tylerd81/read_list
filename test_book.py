import book

def main():

    test_book = book.Book(
        'Test Title',
        'Mr Author',
        987,
        '2018-01-15')

    s = test_book.to_save_string()
    print(s)

    new_book = book.Book(save_string=s)
    s = new_book.to_save_string()
    print('Second Book:')
    print(s)

    print('Percent Read: {}%\n'.format(new_book.get_percent_read()))

    new_book.set_current_page(651)

    print('Percent Read: {}%\n'.format(new_book.get_percent_read()))


if __name__ == '__main__':
    main()
