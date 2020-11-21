import unittest
import doubly_list


class DoublyListTestCase(unittest.TestCase):
    def test_append(self):
        self.assertEqual(3, self.mylist.size)
        self.assertEqual(2, self.mylist.get_index(2))

    def test_pop(self):
        self.assertEqual(2, self.mylist.pop())
        self.assertEqual(2, self.mylist.size)

    def test_isEmpty(self):
        newlist = doubly_list.DoublyLinkedList()
        self.assertTrue(newlist.isEmpty())

    def setUp(self):
        self.mylist = doubly_list.DoublyLinkedList()
        for i in range(3):
            self.mylist.append(i)



if __name__ == '__main__':
    unittest.main()
