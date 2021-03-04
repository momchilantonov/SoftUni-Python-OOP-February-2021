from random import choice


class RandomList(list):
    def get_random_element(self):
        element_to_remove = choice(self)
        return element_to_remove


ll = RandomList([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(ll.get_random_element())
