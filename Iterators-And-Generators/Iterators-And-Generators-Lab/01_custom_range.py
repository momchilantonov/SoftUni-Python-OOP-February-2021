class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            temp = self.start
            return temp
        raise StopIteration()


# class custom_range:
#     def __init__(self, start, end):
#         self.start = star
#         self.end = end
#         self.counter = self.start-1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter == self.end+1:
#             raise StopIteration()
#         return self.counter
