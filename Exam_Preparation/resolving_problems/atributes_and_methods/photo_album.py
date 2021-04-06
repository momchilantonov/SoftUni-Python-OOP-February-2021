class PhotoAlbum:
    MAX_LABELS = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.current_page = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4
        return cls(pages)

    def add_photo(self, label):
        if len(self.photos[self.current_page]) == PhotoAlbum.MAX_LABELS:
            self.current_page += 1
        if self.current_page >= self.pages:
            return "No more free spots"
        self.photos[self.current_page].append(label)
        return f"{label} photo added successfully on page " \
               f"{self.current_page+1} slot {len(self.photos[self.current_page])}"

    def display(self):
        result = ""
        for current_page in self.photos:
            result += "-" * 11+"\n"
            for idx in range(len(current_page)):
                if idx == len(current_page)-1:
                    result += "[]"
                else:
                    result += "[] "
            result += "\n"
        result += "-" * 11+"\n"
        return result


# class PhotoAlbum:
#     def __init__(self, pages):
#         self.pages = pages
#         self.photos = [[] for _ in range(self.pages)]
#         self.current_page = 0
#
#     @classmethod
#     def from_photos_count(cls, photos_count):
#         return cls(photos_count // 4)
#
#     def add_photo(self, label):
#         try:
#             if len(self.photos[self.current_page]) == 4:
#                 self.current_page += 1
#         except:
#             return "No more free spots"
#         if self.current_page >= self.pages:
#             return "No more free spots"
#         self.photos[self.current_page].append(label)
#         return f"{label} photo added successfully on current_page {self.current_page+1} slot {len(self.photos[self.current_page])}"
#
#     def display(self):
#         result = ""
#         for current_page in self.photos:
#             result += "-" * 11+"\n"
#             for idx in range(len(current_page)):
#                 if idx == len(current_page)-1:
#                     result += "[]"
#                 else:
#                     result += "[] "
#             result += "\n"
#         result += "-" * 11+"\n"
#         return result


album = PhotoAlbum(2)
# print(album.__dict__)
# album2 = PhotoAlbum.from_photos_count(8)
# print(album2.__dict__)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
# print(album.add_photo("prom"))
# print(album.add_photo("asd"))
# print(album.add_photo("dsa"))

print(album.display())
