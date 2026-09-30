class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # represent the lru cache with
        # a linked list so we can easily order and reorder keys based on recent usage
        # and a dictionary of key -> (value, node in linked list)
        # node: { key, prev, next }
        self.capacity = capacity
        self.hashmap = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_to_tail(self, node):
        prev = self.tail.prev
        
        prev.next = node
        node.prev = prev

        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]

        self.remove(node)
        self.add_to_tail(node)

        return node.value

    def put(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value

            self.remove(node)
            self.add_to_tail(node)

        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.add_to_tail(node)

        if len(self.hashmap) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.hashmap[lru.key]