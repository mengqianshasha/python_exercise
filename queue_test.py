import unittest
from myqueue import MyQueue

class QueueTestCase(unittest.TestCase):
    def test_enqueue(self):
        queue = MyQueue()
        queue.enqueue(1)
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue.peak())
        self.assertEqual('Queue[1]', str(queue))

    def test_dequeue(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(1,queue.dequeue())
        self.assertEqual("Queue[2, 3]",str(queue))

if __name__ == '__main__':

    unittest.main()
