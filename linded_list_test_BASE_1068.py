import unittest
from linked_list import Node
from linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def test_append(self):
        node1 = Node(1)
        node2 = Node(2)
        link = LinkedList()
        link.append(node1)
        link.append(node2)
        self.assertEqual(2, link.head.next.next.value)
        self.assertEqual(2, link.size)

    def test_pop(self):
        node1 = Node(1)
        node2 = Node(2)
        link = LinkedList()
        link.append(node1)
        link.append(node2)
        self.assertEqual(2, link.pop())
        self.assertEqual(1, link.size)

    def test_get_index(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        link = LinkedList()
        link.append(node1)
        link.append(node2)
        link.append(node3)
        self.assertEqual(2, link.get_index(1))

    def test_delete(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        link = LinkedList()
        link.append(node1)
        link.append(node2)
        link.append(node3)
        link.delete(1)
        self.assertEqual(3, link.head.next.next.value)
        self.assertEqual(2, link.size)

    def test_isEmpty(self):
        link = LinkedList()
        self.assertTrue(link.isEmpty())


if __name__ == '__main__':
    unittest.main()
