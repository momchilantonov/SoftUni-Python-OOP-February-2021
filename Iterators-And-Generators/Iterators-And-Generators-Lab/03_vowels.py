class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels_list = ["a", "e", "i", "o", "u", "y"]
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.text):
            temp_index = self.current_index
            self.current_index += 1
            if self.text[temp_index].lower() in self.vowels_list:
                return self.text[temp_index]
            else:
                return self.__next__()
        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
