class dictionary_iter:
    def __init__(self, my_dict):
        self.my_dict = my_dict
        self.counter = 0
        self.keys = list(self.my_dict.keys())
        self.values = list(self.my_dict.values())

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.my_dict):
            key = self.keys[self.counter]
            val = self.values[self.counter]
            self.counter += 1
            return key, val
        raise StopIteration()




result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
