# from topic import Topic
# from category import Category
# from document import Document

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ""
        for document in self.documents:
            result += document.__repr__()+"\n"
        return result

    def get_category_by_id(self, category_id):
        return [cat for cat in self.categories if cat.id == category_id][0]

    def get_topic_by_id(self, topic_id):
        return [t for t in self.topics if t.id == topic_id][0]

    def get_document_by_id(self, document_id):
        return [doc for doc in self.documents if doc.id == document_id][0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.get_category_by_id(category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_topic_by_id(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.get_document_by_id(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_category_by_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_topic_by_id(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_document_by_id(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.get_document_by_id(document_id)
        return document.__repr__()


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)

# import unittest
#
#
# class TestDocumentManagement(unittest.TestCase):
#     def setUp(self):
#         self.c = Category(1, "C")
#         self.t = Topic(1, "T", "C:\\user")
#         self.d = Document(1, 1, 1, "D")
#         self.s = Storage()
#
#     def test_category_init(self):
#         self.assertEqual(self.c.id, 1)
#         self.assertEqual(self.c.name, "C")
#
#     def test_category_edit(self):
#         self.c.edit("new")
#         self.assertEqual(self.c.name, "new")
#
#     def test_category_repr(self):
#         self.assertEqual(str(self.c), "Category 1: C")
#
#     def test_document_init(self):
#         self.assertEqual(self.d.id, 1)
#         self.assertEqual(self.d.category_id, 1)
#         self.assertEqual(self.d.topic_id, 1)
#         self.assertEqual(self.d.file_name, "D")
#         self.assertEqual(self.d.tags, [])
#
#     def test_document_from_insances(self):
#         doc = Document.from_instances(1, self.c, self.t, "Doc")
#         self.assertEqual(doc.id, 1)
#         self.assertEqual(doc.category_id, 1)
#         self.assertEqual(doc.topic_id, 1)
#         self.assertEqual(doc.file_name, "Doc")
#         self.assertEqual(doc.tags, [])
#
#     def test_document_add_tag(self):
#         self.d.add_tag("tag")
#         self.d.add_tag("tag")
#         self.assertEqual(self.d.tags, ["tag"])
#
#     def test_document_remove_tag(self):
#         self.d.add_tag("tag")
#         self.d.add_tag("tag")
#         self.d.remove_tag("tag")
#         self.assertEqual(self.d.tags, [])
#
#     def test_document_edit(self):
#         self.d.edit("new")
#         self.assertEqual(self.d.file_name, "new")
#
#     def test_document_repr(self):
#         self.d.add_tag("tag")
#         self.assertEqual(str(self.d), 'Document 1: D; category 1, topic 1, tags: tag')
#
#     def test_topic_init(self):
#         self.assertEqual(self.t.id, 1)
#         self.assertEqual(self.t.id, 1)
#         self.assertEqual(self.t.storage_folder, "C:\\user")
#
#     def test_topic_edit(self):
#         self.t.edit("new topic", "new folder")
#         self.assertEqual(self.t.topic, "new topic")
#         self.assertEqual(self.t.storage_folder, "new folder")
#
#     def test_topic_repr(self):
#         self.assertEqual(str(self.t), "Topic 1: T in C:\\user")
#
#     def test_storage_init(self):
#         self.assertEqual(self.s.categories, [])
#         self.assertEqual(self.s.topics, [])
#         self.assertEqual(self.s.documents, [])
#
#     def test_storage_add_category(self):
#         self.s.add_category(self.c)
#         self.s.add_category(self.c)
#         self.assertEqual(self.s.categories, [self.c])
#
#     def test_storage_add_topic(self):
#         self.s.add_topic(self.t)
#         self.s.add_topic(self.t)
#         self.assertEqual(self.s.topics, [self.t])
#
#     def test_storage_add_document(self):
#         self.s.add_document(self.d)
#         self.s.add_document(self.d)
#         self.assertEqual(self.s.documents, [self.d])
#
#     def test_storage_edit_category(self):
#         self.s.add_category(self.c)
#         self.s.edit_category(1, "new")
#         self.assertEqual(self.s.categories[0].name, "new")
#
#     def test_storage_edit_topic(self):
#         self.s.add_topic(self.t)
#         self.s.edit_topic(1, "new", "new storage")
#         self.assertEqual(self.s.topics[0].topic, "new")
#         self.assertEqual(self.s.topics[0].storage_folder, "new storage")
#
#     def test_storage_edit_document(self):
#         self.s.add_document(self.d)
#         self.s.edit_document(1, "new")
#         self.assertEqual(self.s.documents[0].file_name, "new")
#
#     def test_storage_delete_category(self):
#         self.s.add_category(self.c)
#         self.s.delete_category(1)
#         self.assertEqual(self.s.categories, [])
#
#     def test_storage_delete_topic(self):
#         self.s.add_topic(self.t)
#         self.s.delete_topic(1)
#         self.assertEqual(self.s.topics, [])
#
#     def test_storage_delete_document(self):
#         self.s.add_document(self.d)
#         self.s.delete_document(1)
#         self.assertEqual(self.s.documents, [])
#
#     def test_storage_repr(self):
#         self.s.add_category(self.c)
#         self.s.add_topic(self.t)
#         self.s.add_document(self.d)
#         expected = str(self.s).strip('\n')
#         self.assertEqual(expected, "Document 1: D; category 1, topic 1, tags: ")
#
#
# if __name__ == "__main__":
#     unittest.main()
