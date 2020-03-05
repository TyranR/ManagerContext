import unittest
from unittest.mock import patch
import json
from main import add

test_documents = []
with open('../fixtures/documents.json', 'r', encoding='utf-8') as \
        out_docs:
    test_documents.extend(json.load(out_docs))

test_directories = {}
with open('../fixtures/directories.json', 'r', encoding='utf-8') as \
        out_dirs:
    test_directories.update(json.load(out_dirs))


@patch('main.documents', test_documents, create=True)
@patch('main.directories', test_directories, create=True)
class TestSecretaryProgram(unittest.TestCase):

    # def setUp(self):
    #     self.test_documents = []
    #     with open('../fixtures/documents.json', 'r', encoding='utf-8') as \
    #             out_docs:
    #         self.test_documents.extend(json.load(out_docs))
    #     self.test_directories = {}
    #     with open('../fixtures/directories.json', 'r', encoding='utf-8') as \
    #             out_dirs:
    #         self.test_directories.update(json.load(out_dirs))
    #

    @patch('main.input', side_effect =['1','1','1','1'])
    def test_add_document(self, side_effect):
        start_len = len(test_documents)
        add()
        self.assertGreater(len(test_documents), start_len)


if __name__ == '__main__':
    unittest.main()
