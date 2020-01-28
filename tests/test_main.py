import unittest
import json
from main import people
from main import add


def setUpModule():
    test_documents = []
    test_directories = {}


class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        self.test_documents = []
        with open('../fixtures/documents.json', 'r', encoding='utf-8') as \
                out_docs:
            self.test_documents.extend(json.load(out_docs))
        self.test_directories = {}
        with open('../fixtures/directories.json', 'r', encoding='utf-8') as \
                out_dirs:
            self.test_directories.update(json.load(out_dirs))

    def tearDown(self):
        pass

    def test_people_check(self):
        pass

    def test_add_document(self):
        pass

    def test_something(self):
        # self.assertEqual(True, False)
        pass


if __name__ == '__main__':
    unittest.main()
