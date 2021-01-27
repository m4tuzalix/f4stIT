import unittest
from Excel_class.excel_reporting import Excel
class TestExcelReporting(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.excel = Excel()
    @classmethod
    def tearDown(cls):
        pass
    def test00_add_data(self):
        data = ["one", "two", "three"]
        key_words = ["one"]
        self.assertEqual(self.excel.add_data(data, key_words), True)
