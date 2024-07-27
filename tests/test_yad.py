import unittest
from API_yandex import create_folder_YA


class TestYaApi(unittest.TestCase):

    def test_success_create_folder(self):
        self.assertEqual(create_folder_YA('test'), 201)