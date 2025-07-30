class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    # the __str__ method is equivalent to the toString method in Java,
    # and allows us to customize the print(object) behavior:
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_pages}"

    # the __eq__ method allows us to check if two objects are equal, based on our preferences
    # (That is because by default, it checks if two objects reference the same memory address,
    # but we can customize the behavior)
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # we can customize the behavior of < using the less than operator:
    # __lt__
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # same as the > operator, there is a greater than magic method:
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # to use the add operator, there is the add magic method:
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages}"

    # we can also customize the behavior of certain operators, such as "in":
    def __contains__(self, item):
        return item in self.title.lower() or item in self.author.lower()

    # the __getitem__ method allows us to customize the behavior of the indexing operator
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return None


def main():
    # Whenever we create a new object, the __init__ method gets automatically called
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    book2 = Book("Harry Potter", "J.K. Rowling", 223)

    print(book1)
    print(book2)

    # to access the __eq__ method, we use the == operator:
    print(book1 == book2)

    # to access the __lt__ method, we use the < operator:
    print(book1 < book2)

    # to access the __gt__ method, we use the > operator:
    print(book1 > book2)

    # to access the __add__ method, we'll use the + operator:
    print(book1 + book2)

    # to access the __contains__ method, we'll use the in operator:
    print("Rowling" in book2)

    # we can also customize the behavior of the indexing, in this case by using a key:
    print(book1["title"])
    print(book1["author"])
    print(book1["num_pages"])

if __name__ == "__main__":
    main()