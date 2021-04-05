from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # author:name
        self.rented_books = {}  # user:name:days_left

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    def change_username(self, user_id, new_username):
        for user in self.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username " \
                           "- it should be different than the username used so far!"
                user.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"


# user = User(12, 'Peter')
# library = Library()
# library.add_user(user)
# print(library.add_user(user))
# library.remove_user(user)
# print(library.remove_user(user))
# library.add_user(user)
# print(library.change_username(2, 'Igor'))
# print(library.change_username(12, 'Peter'))
# print(library.change_username(12, 'George'))
# [print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
#                                                 'The Prisoner of Azkaban',
#                                                 'The Goblet of Fire',
#                                                 'The Order of the Phoenix',
#                                                 'The Half-Blood Prince',
#                                                 'The Deathly Hallows']})
# user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
# print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
# print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
# user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
#
# user = User(12, 'Peter')
# library = Library()
# library.add_user(user)
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
#                                                 'The Prisoner of Azkaban',
#                                                 'The Goblet of Fire',
#                                                 'The Order of the Phoenix',
#                                                 'The Half-Blood Prince',
#                                                 'The Deathly Hallows']})
# user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library)
# print(user)
#
# import unittest
#
#
# class TestsUser(unittest.TestCase):
#     def setUp(self):
#         self.user = User(12, 'Valentina')
#         self.library = Library()
#
#     def test_init(self):
#         self.assertEqual(self.user.user_id, 12)
#         self.assertEqual(self.user.username, 'Valentina')
#         self.assertEqual(self.user.books, [])
#
#     def test_get_book_method_with_book_available_in_the_library_should_add_it_in_the_books_list(self):
#         self.library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Deathly Hallows',
#                                                              'Harry Potter and the Order of the Phoenix']})
#         result = self.user.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, self.library)
#         self.assertEqual(result, 'Harry Potter and the Deathly Hallows successfully rented for the next 17 days!')
#         self.assertEqual(self.user.books, ["Harry Potter and the Deathly Hallows"])
#         self.assertEqual(self.library.rented_books, {'Valentina': {'Harry Potter and the Deathly Hallows': 17}})
#         self.assertEqual(self.library.books_available, {'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                                         'Harry Potter and the Philosopher\'s Stone',
#                                                                         'Harry Potter and the Order of the Phoenix']})
#
#     def test_get_book_method_with_book_already_rented_should_return_a_message(self):
#         self.library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Deathly Hallows',
#                                                              'Harry Potter and the Order of the Phoenix']})
#         self.user.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, self.library)
#         second_user = User(13, 'Peter')
#         result = second_user.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, self.library)
#         self.assertEqual(result,
#                          'The book "Harry Potter and the Deathly Hallows" is already rented and will be available in 17 days!')
#         self.assertEqual(self.user.books, ["Harry Potter and the Deathly Hallows"])
#         self.assertEqual(second_user.books, [])
#         self.assertEqual(self.library.rented_books, {'Valentina': {'Harry Potter and the Deathly Hallows': 17}})
#         self.assertEqual(self.library.books_available, {'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                                         'Harry Potter and the Philosopher\'s Stone',
#                                                                         'Harry Potter and the Order of the Phoenix']})
#
#     def test_return_book_method_with_rented_book_should_remove_from_user_records_and_add_it_back_to_library_records(
#             self):
#         self.library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Deathly Hallows',
#                                                              'Harry Potter and the Order of the Phoenix']})
#         self.user.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 3, self.library)
#         self.user.get_book('J.K.Rowling', 'Harry Potter and the Order of the Phoenix', 12, self.library)
#         self.assertEqual(self.user.books,
#                          ['Harry Potter and the Deathly Hallows', 'Harry Potter and the Order of the Phoenix'])
#         self.user.return_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', self.library)
#         self.assertEqual(self.user.books, ['Harry Potter and the Order of the Phoenix'])
#         self.assertEqual(self.library.books_available, {'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                                         'Harry Potter and the Deathly Hallows']})
#         self.assertEqual(self.library.rented_books, {'Valentina': {'Harry Potter and the Order of the Phoenix': 12}})
#
#     def test_return_book_method_with_book_NOT_rented_by_the_user_should_return_message(self):
#         self.library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Deathly Hallows',
#                                                              'Harry Potter and the Order of the Phoenix']})
#         self.user.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 3, self.library)
#         result = self.user.return_book('J.K.Rowling', 'Harry Potter and the Order of the Phoenix', self.library)
#         self.assertEqual(result, f'Valentina doesn\'t have this book in his/her records!')
#
#     def test_info_method_should_return_sorted_books_list(self):
#         self.library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosophers Stone',
#                                                              'Harry Potter and the Deathly Hallows',
#                                                              'Harry Potter and the Order of the Phoenix']})
#         self.user.get_book('J.K.Rowling', 'Harry Potter and the Order of the Phoenix', 3, self.library)
#         self.user.get_book('J.K.Rowling', 'Harry Potter and the Philosophers Stone', 3, self.library)
#         self.user.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 3, self.library)
#
#         result = self.user.info()
#         self.assertEqual(result,
#                          "Harry Potter and the Deathly Hallows, Harry Potter and the Order of the Phoenix, Harry Potter and the Philosophers Stone")
#
#     def test_init(self):
#         self.assertEqual(self.library.user_records, [])
#         self.assertEqual(self.library.books_available, {})
#         self.assertEqual(self.library.rented_books, {})
#
#     def test_add_user_already_registered_in_the_library_should_return_message(self):
#         user = User(12, 'Valentina')
#         library = Library()
#         library.add_user(user)
#         result = library.add_user(user)
#         self.assertEqual(result, 'User with id = 12 already registered in the library!')
#
#     def test_add_user_method_with_valid_data_should_update_records_properly(self):
#         user = User(12, 'Valentina')
#         library = Library()
#         library.add_user(user)
#         library.add_user(User(13, 'Peter'))
#         self.assertEqual(library.user_records[0].__str__(), '12, Valentina, []')
#         self.assertEqual(library.user_records[1].__str__(), '13, Peter, []')
#
#     def test_remove_user_method_with_valid_data_should_update_library_records_properly(self):
#         user = User(12, 'Valentina')
#         library = Library()
#         library.add_user(user)
#         library.add_user(User(13, 'Peter'))
#         library.remove_user(user)
#         self.assertEqual(library.user_records[0].__str__(), '13, Peter, []')
#
#     def test_remove_user_method_with_user_not_registered_should_return_message(self):
#         v = User(12, 'Valentina')
#         p = User(13, 'Peter')
#         library = Library()
#         library.add_user(v)
#         result = library.remove_user(p)
#         self.assertEqual(result, 'We could not find such user to remove!')
#
#     def test_change_username_method_with_user_id_not_included_in_library_records_should_return_message(self):
#         v = User(12, 'Valentina')
#         p = User(13, 'Peter')
#         library = Library()
#         library.add_user(v)
#         result = library.change_username(13, 'George')
#         self.assertEqual(result, 'There is no user with id = 13!')
#
#     def test_change_username_method_with_user_id_included_in_library_records_but_provided_new_username_is_the_same_should_return_message(
#             self):
#         v = User(12, 'Valentina')
#         p = User(13, 'Peter')
#         library = Library()
#         library.add_user(v)
#         result = library.change_username(12, 'Valentina')
#         self.assertEqual(result,
#                          'Please check again the provided username - it should be different than the username used so far!')
#
#     def test_change_username_method_with_valid_data_should_return_message_and_update_library_records(self):
#         v = User(12, 'Valentina')
#         p = User(13, 'Peter')
#         library = Library()
#         library.add_user(v)
#         result = library.change_username(12, 'Violeta')
#         self.assertEqual(result, 'Username successfully changed to: Violeta for userid: 12')
#         self.assertEqual(library.user_records[0].__str__(), '12, Violeta, []')
#
#
# if __name__ == "__main__":
#     unittest.main()
