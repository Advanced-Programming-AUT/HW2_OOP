class BookClassForLibrarySystem:
    def __init__(self, title_of_book_input, author_of_book_input):
        self.title_of_the_book_attribute = title_of_book_input
        self.author_of_the_book_attribute = author_of_book_input
        self.current_status_of_book_attribute = "Available"

    def borrow_book_method(self):
        if self.current_status_of_book_attribute == "Available":
            self.current_status_of_book_attribute = "Borrowed"
            return True
        return False

    def return_book_method(self):
        self.current_status_of_book_attribute = "Available"
        return True

    def get_book_details_method(self):
        details_string = ""
        details_string += self.title_of_the_book_attribute + " by " + self.author_of_the_book_attribute
        details_string += " (" + self.current_status_of_book_attribute + ")"
        return details_string