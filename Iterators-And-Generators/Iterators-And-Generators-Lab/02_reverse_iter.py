class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current_index = len(self.iterable)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= 0:
            temp_index = self.current_index
            self.current_index -= 1
            return self.iterable[temp_index]
        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
