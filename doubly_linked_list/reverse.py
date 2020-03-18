from doubly_linked_list import DoublyLinkedList

def reverse(dll):
    current = dll.head
    new = current.next
    current.next = None
    while new is not None:
        prev = current
        current = new
        current.next = prev
        new = current.next