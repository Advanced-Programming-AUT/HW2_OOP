from book import BookClassForLibrarySystem


class LibraryManagementSystemClass:
    def __init__(self):
        self.list_of_all_books_in_library_attribute = []

    def add_new_book_to_library_method(self, book_title_input, book_author_input):
        new_book_object = BookClassForLibrarySystem(book_title_input, book_author_input)
        self.list_of_all_books_in_library_attribute.append(new_book_object)
        return new_book_object

    def borrow_book_from_library_method(self, book_title_input):
        book_found = None
        for book_item in self.list_of_all_books_in_library_attribute:
            if book_item.title_of_the_book_attribute == book_title_input:
                book_found = book_item
                break

        if book_found:
            if book_found.borrow_book_method():
                return True
        return False

    def return_book_to_library_method(self, book_title_input):
        book_found = None
        for book_item in self.list_of_all_books_in_library_attribute:
            if book_item.title_of_the_book_attribute == book_title_input:
                book_found = book_item
                break

        if book_found:
            if book_found.return_book_method():
                return True
        return False

    def show_all_books_in_library_method(self):
        books_info_string = "Library Books\n"
        for book_item in self.list_of_all_books_in_library_attribute:
            books_info_string += book_item.get_book_details_method() + "\n"
        return books_info_string