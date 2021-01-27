import unittest
from Pages.main import JustJoinIt
from Selectors.page_selectors import justJoinIt as selector

class test_PageObject(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.object = JustJoinIt()
    @classmethod
    def tearDown(cls):
        pass

    def test00_fetching_data(self):
        result = self.object.fetching_data()
        self.assertIsInstance(result, list)
        