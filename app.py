from models import Base, session, Book, engine
import datetime
import csv


# add books to the database
# edit books
# delete books
# search books
# data cleaning
# loop - run program


def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1) Add book
        \r2) View all books
        \r3) Search for a book
        \r4) Book analysis
        \r5) Exit''')
        choice = input('What would you like to do?')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''Please choose one of the options above.
            \rA number between 1 and 5.
            \rPress enter to try again.''')


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    print(split_date)
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    print(day)
    year = int(split_date[2])
    return datetime.date(year, month, day)


def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)


def app():
    app_running = True
    while app_running:
        choice = menu()

        if choice == '1':
            # Add Book
            pass
        elif choice == '2':
            # View books
            pass
        elif choice == '3':
            # Search book
            pass
        elif choice == '4':
            # Analysis
            pass
        else:
            print('GOODBYE')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # app()
    # add_csv()
    clean_date('October 25, 2017')