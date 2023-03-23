from models import Base, session, Book, engine


# import models file
# main menu - add, search, analysis, exit, view
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
    app()