import unittest
from my_awesome_lib.data_utils import find_max, find_min 

class TestDataUtils(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3]), 3)

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3]), 1)

if __name__ == '__main__':
    unittest.main()
