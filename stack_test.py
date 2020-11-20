import unittest
from stack import Stack


class StackTestCase(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual('Stack[1]', str(stack))
        self.assertEqual(1, stack.size())
        self.assertEqual(1, stack.top())

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())


if __name__ == '__main__':
    unittest.main()
