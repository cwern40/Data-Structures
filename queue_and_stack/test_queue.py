import unittest
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# from dll_queue import Queue

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size >= 1:
             self.size -= 1
        return self.storage.remove_from_head()
            
    def len(self):
        return self.size

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_len_returns_0_for_empty_queue(self):
        self.assertEqual(self.q.len(), 0)

    def test_len_returns_correct_length_after_enqueue(self):
        self.assertEqual(self.q.len(), 0)
        self.q.enqueue(2)
        self.assertEqual(self.q.len(), 1)
        self.q.enqueue(4)
        self.assertEqual(self.q.len(), 2)
        self.q.enqueue(6)
        self.q.enqueue(8)
        self.q.enqueue(10)
        self.q.enqueue(12)
        self.q.enqueue(14)
        self.q.enqueue(16)
        self.q.enqueue(18)
        self.assertEqual(self.q.len(), 9)

    def test_empty_dequeue(self):
        self.assertIsNone(self.q.dequeue())
        self.assertEqual(self.q.len(), 0)

    def test_dequeue_respects_order(self):
        self.q.enqueue(100)
        self.q.enqueue(101)
        self.q.enqueue(105)
        self.assertEqual(self.q.dequeue(), 100)
        self.assertEqual(self.q.len(), 2)
        self.assertEqual(self.q.dequeue(), 101)
        self.assertEqual(self.q.len(), 1)
        self.assertEqual(self.q.dequeue(), 105)
        self.assertEqual(self.q.len(), 0)
        self.assertIsNone(self.q.dequeue())
        self.assertEqual(self.q.len(), 0)

if __name__ == '__main__':
    unittest.main()


        
