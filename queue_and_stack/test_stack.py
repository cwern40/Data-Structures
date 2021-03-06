import unittest
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# from dll_stack import Stack

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_len_returns_0_for_empty_stack(self):
        self.assertEqual(self.s.len(), 0)

    def test_len_returns_correct_length_after_push(self):
        self.assertEqual(self.s.len(), 0)
        self.s.push(2)
        self.assertEqual(self.s.len(), 1)
        self.s.push(4)
        self.assertEqual(self.s.len(), 2)
        self.s.push(6)
        self.s.push(8)
        self.s.push(10)
        self.s.push(12)
        self.s.push(14)
        self.s.push(16)
        self.s.push(18)
        self.assertEqual(self.s.len(), 9)

    def test_empty_pop(self):
        self.assertIsNone(self.s.pop())
        self.assertEqual(self.s.len(), 0)

    def test_pop_respects_order(self):
        self.s.push(100)
        self.s.push(101)
        self.s.push(105)
        self.assertEqual(self.s.pop(), 105)
        self.assertEqual(self.s.len(), 2)
        self.assertEqual(self.s.pop(), 101)
        self.assertEqual(self.s.len(), 1)
        self.assertEqual(self.s.pop(), 100)
        self.assertEqual(self.s.len(), 0)
        self.assertIsNone(self.s.pop())
        self.assertEqual(self.s.len(), 0)


if __name__ == '__main__':
    unittest.main()
