import unittest
from linked_list import *


class LinkedListTestCase(unittest.TestCase):
    def test_append(self):
        link = LinkedList()
        link.append(1)
        link.append(2)
        self.assertEqual(2, link.head.next.next.value)
        self.assertEqual(2, link.size)

    def test_pop(self):
        link = LinkedList()
        link.append(1)
        link.append(2)
        self.assertEqual(2, link.pop())
        self.assertEqual(1, link.size)

    def test_get_index(self):
        link = LinkedList()
        link.append(1)
        link.append(2)
        link.append(3)
        self.assertEqual(2, link.get_value(1))

    def test_delete(self):
        link = LinkedList()
        link.append(1)
        link.append(2)
        link.append(3)
        link.delete(1)
        self.assertEqual(3, link.head.next.next.value)
        self.assertEqual(2, link.size)

    def test_isEmpty(self):
        link = LinkedList()
        self.assertTrue(link.is_empty())

    def test_has_cycle(self):
        link = LinkedList()
        self.assertFalse(link.has_cycle())
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        link.__insert__after__(link.head, node1)
        link.__insert__after__(node1, node2)
        link.__insert__after__(node2, node3)
        self.assertFalse(link.has_cycle())
        node3.next = node2
        self.assertTrue(link.has_cycle())

    def test_reverse(self):
        link = LinkedList()
        link.append(1)
        link.append(2)
        link.append(3)
        link.reverse()
        self.assertEqual(3, link.get_value(0))
        self.assertEqual(2, link.get_value(1))
        self.assertEqual(1, link.get_value(2))

    def test_reverse_between(self):
        link = LinkedList()
        with self.assertRaises(LinkedListEmptyError):
            link.reverse_between(0, 0)

        link.append(1)
        link.reverse_between(0, 0)
        self.assertEqual(1,link.get_value(0))

        link.append(2)
        link.append(3)
        link.reverse_between(1, 2)
        self.assertEqual(3, link.get_value(1))
        self.assertEqual(2, link.get_value(2))



if __name__ == '__main__':
    unittest.main()
