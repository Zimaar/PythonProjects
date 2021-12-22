class Book:

    # Constructor for initializing a book
    def __init__(self, title, author, isbn, num):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.num = num  # num is the ID of the book used for updating/deleting
        # it is essentially the position of the book in the list

    # Defining __str__ to print details of each book
    def __str__(self):
        return f"{self.title} is written by {self.author}.\nISBN: {self.isbn}\nID: {self.num}"

    # Setters for each detail
    def update_title(new_title):
        title = new_title

    def update_author(new_author):
        author = new_author

    def update_isbn(new_isbn):
        isbn = new_isbn

    def update_num(new_num):
        num = new_num

    # Updates all details at once
    def update_all(new_title, new_author, new_isbn):
        title = new_title
        author = new_author
        isbn = new_isbn


class Library:

    def __init__(self, book_list):
        self.book_list = book_list

    # Adds book to book_list
    def add_book(self, title, author, isbn):

        if not self.book_list:  # NUM ID is defined as position of book in list
            num = 0  # so this if statement checks if the list is empty
        else:  # and if not, it sets itself to the end of the list
            num = len(self.book_list)

        new_book = Book(title, author, isbn, num)
        self.book_list.append(new_book)

    # Removes a book from the book list using pop()
    def delete_book(self, num):
        self.book_list.pop(num)

    # Updates all parts of the book
    def update_book_all(self, num, new_title, new_author, new_isbn):
        self.book_list[num].update_all(new_title, new_author, new_isbn)

    # Next three methods update individual parts of the book
    def update_title(self, num, new_title):
        self.book_list[num].update_title(new_title)

    def update_author(self, num, new_author):
        self.book_list[num].update_author(new_author)

    def update_isbn(self, num, new_isbn):
        self.book_list[num].update_isbn(new_isbn)

    # Prints the details of specified book
    def view_book(self, num):
        print(self.book_list[num])

    # Prints all books in the library
    def view_library(self):
        for book in self.book_list:
            print(f"{book} \n")


# Main controller for program
def main():
    book_list = []  # instantiating book list
    library = Library(book_list)

    # While loop allows for user menu
    while (True):
        print("Welcome to the Library")
        choice = int(input(
            "Would you like to\n1) Add a Book\n2) Remove a Book\n3) View a Book\n4) View Library\n5) Update a Book"))

        if choice == 1:
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            library.add_book(title, author, isbn)
            print(f"Book ID Number is {len(library.book_list)}")
            print("Book Added")

        if choice == 2:
            num = int(input("Enter the Book ID: "))
            library.delete_book(num)
            print("Book Removed")

        if choice == 3:
            num = int(input("Enter the Book ID: "))
            library.view_book(num)

        if choice == 4:
            library.view_library()

        if choice == 5:
            num = int(input("Enter the Book ID: "))
            choice2 = int(input("Would you like to change\n1) Title\n2) Author\n3) ISBN\n4) All Details\n"))

            # Nested if loop for further options
            if choice2 == 1:
                new_title = input("Enter the new title: ")
                library.update_title(num, new_title)

            if choice2 == 2:
                new_author = input("Enter the new author: ")
                library.update_author(num, new_author)

            if choice2 == 3:
                new_isbn = input("Enter the new ISBN: ")
                library.update_isbn(num, new_isbn)

            if choice2 == 4:
                new_title = input("Enter the new title: ")
                new_author = input("Enter the new author: ")
                new_isbn = input("Enter the new ISBN: ")
                library.update_book_all(num, new_title, new_author, new_isbn)

        else:
            print("Please choose a valid option of a number between 1 and 5.")


main()

