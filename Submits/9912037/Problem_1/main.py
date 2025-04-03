from library import LibraryManagementSystemClass

library_system_instance = LibraryManagementSystemClass()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Exit")

    user_choice_input = input("Enter your choice: ")

    if user_choice_input == "1":
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        new_book = library_system_instance.add_new_book_to_library_method(book_title, book_author)
        print("Added " + new_book.title_of_the_book_attribute + " by " + new_book.author_of_the_book_attribute)

    elif user_choice_input == "2":
        book_title = input("Enter book title to borrow: ")
        if library_system_instance.borrow_book_from_library_method(book_title):
            print("Borrowed " + book_title)
        else:
            print("Book not available or not found!")

    elif user_choice_input == "3":
        book_title = input("Enter book title to return: ")
        if library_system_instance.return_book_to_library_method(book_title):
            print("Returned " + book_title)
        else:
            print("Book not found!")

    elif user_choice_input == "4":
        all_books_info = library_system_instance.show_all_books_in_library_method()
        print(all_books_info)

    elif user_choice_input == "5":
        break

    else:
        print("Invalid choice!")