from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.size = 0
        self.order = DoublyLinkedList()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # item = self.storage.get(key, None)
        # if item is not None:
        #     new_key = {key: item}
        #     self.storage.pop(key)
        #     self.storage.update(new_key)
        # return item
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # item = {key: value}
        # same = False
        # if self.size == 0:
        #     self.size += 1
        #     return self.storage.update(item)
        # for current_key in self.storage:
        #     if key == current_key:
        #         same = True
        # if same:
        #    return self.storage.update(item) 
        # elif self.size == self.limit:
        #     self.storage.pop(list(self.storage.keys())[0])
        #     return self.storage.update(item)
        # else:
        #     self.size += 1
        #     return self.storage.update(item)
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return
        if self.size == self.limit:
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.size -= 1
        
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1        
