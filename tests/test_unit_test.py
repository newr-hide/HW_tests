import unittest
from unittest import TestCase, mock
from main import check_document_existance, get_doc_owner_name, add_new_doc, delete_doc
from unittest.mock import patch

class Test_main(TestCase):

    # def setUp(self):
    #     self.user_doc_number = "2207 876234"
    #     self.documents = [
    # {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    # {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    # {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]
    #     self.directories = {
    # '1': ['2207 876234', '11-2', '5455 028765'],
    # '2': ['10006'],
    # '3': []}
    #     print('method setUp')

    # def tearDown(self):
    #     print('method tearDown')
    @mock.patch('builtins.input', side_effect=['2207 876234'])
    def test_get_doc_owner_name(self, mock_input):
        self.assertEqual(get_doc_owner_name(), 'Василий Гупкин')
        print("test_get_doc_owner_name")

    @mock.patch('builtins.input', side_effect=['7311', 'pass', 'Гупкин', 2])
    def test_add_new_doc(self, mock_input):
        self.assertEqual(add_new_doc(), 2)
        print('test_add_new_doc')

    @mock.patch('builtins.input', side_effect=['10006'])
    def test_delete_doc(self, mock_input):
        self.assertTrue(delete_doc())

    def test_check_document_existance(self):
        self.user_doc_number = '333 222'
        self.assertFalse(check_document_existance(self.user_doc_number))
        print('test_check_document_existance')