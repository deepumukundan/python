# Use a dictionary for O(1) access
# Use another DS, potentially a linked list whose nodes are the values in the dic
# Every time we put a key-value pair, add it to Tail of LL
# If the dict has more values than capacity, shrink from head
# Move an existing key to tail if it was accessed (during get or put)

class DLLNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val        
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = DLLNode(0,0)
        self.tail = DLLNode(0,0)
        self.head.next = self.tail
        self.head.prev = None
        self.tail.next = None
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        existing_node = self.dict[key]
        self.removeNode(existing_node)
        self.addNode(existing_node)
        return self.dict[key].val

    def put(self, key: int, val: int) -> None:
        # Save new node to tail
        if key in self.dict:
            existing_node = self.dict[key]
            existing_node.val = val
            self.removeNode(existing_node)
            self.addNode(existing_node)
            self.dict[key] = existing_node
        else:
            new_node = DLLNode(key, val)
            self.addNode(new_node)
            self.dict[key] = new_node

        # Evict older nodes
        while len(self.dict) > self.capacity:
            node_to_del = self.head.next
            self.removeNode(node_to_del)
            del self.dict[node_to_del.key]

    def addNode(self, node: DLLNode):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node: DLLNode):
        node.prev.next = node.next
        node.next.prev = node.prev