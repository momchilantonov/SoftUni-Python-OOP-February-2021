from random import randint


class RandomList(list):
    def get_random_element(self):
        index_to_remove = randint(0, len(self))
        return self.pop(index_to_remove)


ll = RandomList([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(ll.get_random_element())