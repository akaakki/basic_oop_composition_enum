from author import Author, Gender
from book import Book



class BookTest:
    def __init__(*args):
        # TODO Initialize authors below
        author1 = Author("Gabriel", "gabriel@email.com", Gender.FLUID)
        author2 = Author("Mandy", "gabriel@email.com", "female")
        author3 = Author("John", "gabriel@email.com", Gender.FLUID)

        print(author1)
        print(author2)
        print(author3)  # Test __str__(self)
        author3.set_email("changedemail@email.com")  # Test email setter
        print("name is: " + author3.get_name())  # Test getter
        print("email is: " + author3.get_email())  # Test getter
        print("gender is: " + author3.get_gender())  # Test getter
        print(
            "Author after changed email: "
            + str(author3)  # pay attention! author3 now has a changed email
        )
        print("========================")

        # TODO Initialize books below
        book1 = Book("Harry Potter 1", author1, 20, 100)
        book2 = Book("Harry Potter 2", author2, 20, 100)
        book3 = Book("Harry Potter 3", author3, 20, 100)

        print(book1)
        print(book2)
        print(book3)

        # Test Getters and Setters
        book3.set_price(29.95)
        book3.set_qty(28)
        print("name is: " + book3.get_name())
        print("price is: " + str(book3.get_price()))
        print("qty is: " + str(book3.get_qty()))
        print("Author is: " + str(book3.get_author()))
        # Author's __str__(self)
        print("Author's name is: " + book3.get_author().get_name())
        print("Author's email is: " + book3.get_author().get_email())
        print("Book after changed price and quantity: " + str(book3))


BookTest()