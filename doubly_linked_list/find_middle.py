from doubly_linked_list import DoublyLinkedList

def find_middle(dll):
    head = dll.head
    tail = dll.tail

    while head != tail and head.next != tail:
        head = head.next
        tail = tail.prev

    return head.value