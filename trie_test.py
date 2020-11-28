import unittest
from trie import *


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        dic = Trie()
        dic.insert('apple')
        self.assertTrue(dic.contains('apple'))
        self.assertTrue(dic.start_with('app'))
        self.assertFalse(dic.contains('app'))

if __name__ == '__main__':
    unittest.main()
