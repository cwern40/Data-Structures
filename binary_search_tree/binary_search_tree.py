import sys
sys.path.append('./queue_and_stack')
from doubly_linked_list import DoublyLinkedList
# from dll_queue import Queue
# from dll_stack import Stack

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
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            change = self.right
            self.right = BinarySearchTree(value)
            self.right.right = change
            return
        if value > self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
        return cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)
        
        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node.value)
        current_nodes = [node]
        next_nodes = []

        while queue.len() is not 0:
            for value in current_nodes:
                if value.left is not None:
                    next_nodes.append(value.left)
                    queue.enqueue(value.left.value)
                if value.right is not None:
                    next_nodes.append(value.right)
                    queue.enqueue(value.right.value)
                queue.dequeue()
            current_nodes = next_nodes
            next_nodes = []

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        queue = Queue()
        queue.enqueue(node.value)
        
        pass
        # print(node.value)

        # if node.left is not None:
        #     self.dft_print(node.left)

        # if node.right is not None:
        #     self.dft_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass