# from dataclasses import dataclass


class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


# @dataclass
# class Book2:
#     name: str
#     author: str
#     pages: int


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

# book2 = Book2("My Book", "Me", 200)
# print(book2.name)
# print(book2.author)
# print(book2.pages)
