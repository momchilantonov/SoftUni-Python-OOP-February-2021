from category import Category
from document import Document
from topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def category_is_in_categories(self, category):
        return category in self.categories

    def topic_is_in_topics(self, topic):
        return topic in self.topics

    def document_is_in_documents(self, document):
        return document in self.documents

    def add_category(self, category):
        if not self.category_is_in_categories(category):
            self.categories.append(category)

    def add_topic(self, topic):
        if not self.topic_is_in_topics(topic):
            self.topics.append(topic)

    def add_document(self, document):
        if not self.document_is_in_documents(document):
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for category in self.categories:
            if category_id == category.id:
                category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for topic in self.topics:
            if topic_id == topic.id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        for document in self.documents:
            if document_id == document.id:
                document.file_name = new_file_name

    def delete_category(self, category_id):
        for category in self.categories:
            if category_id == category.id:
                self.categories.remove(category)

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic_id == topic.id:
                self.topics.remove(topic)

    def delete_document(self, document_id):
        for document in self.documents:
            if document_id == document.id:
                self.documents.remove(document)

    def get_document(self, document_id):
        for document in self.documents:
            if document_id == document.id:
                return document

    def get_document_repr(self):
        for document in self.documents:
            return document.__repr__()

    def __repr__(self):
        return f"{self.get_document_repr()}"


c1 = Category(1, "C")
print(c1)
c1.edit("D")
print(c1)

t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)
storage.edit_category(1, "new")

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
