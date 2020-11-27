import unittest
from binary_search import binary_search


class BinarySearchTestCase(unittest.TestCase):
    def test_binary_search(self):
        sorted_list = [num * 3 for num in range(10)]
        self.assertEqual(-1, binary_search(sorted_list, 10))
        self.assertEqual(4, binary_search(sorted_list, 12))
        self.assertEqual(8, binary_search(sorted_list, 24))
        self.assertEqual(9, binary_search(sorted_list, 27))


if __name__ == '__main__':
    unittest.main()
