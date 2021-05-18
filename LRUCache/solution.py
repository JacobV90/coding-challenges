class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map = {}
        
    def _remove_lru(self):
        key = self.tail.key
        self.tail = self.tail.left
        self.tail.right = None
        self.map.pop(key)
        
    def _prepend_to_head(self, node):
        self.map[node.key] = node
        node.right = self.head
        node.right.left = node
        self.head = node
        self.head.left = None
        
    def _move_to_head(self, node):
        if node.left and node.right:
            tmp_ptr = node.left
            tmp_ptr.right = node.right
            node.right.left = tmp_ptr
            self._prepend_to_head(node)
        elif node.left:
            self.tail = node.left
            self.tail.right = None
            self._prepend_to_head(node)

    def get(self, key: int) -> int:
        if key in self.map:
            matched_node = self.map[key]
            self._move_to_head(matched_node)
            return matched_node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if self.head == None:
            node = Node(key, value)
            self.head = node
            self.tail = node
            self.map[key] = node
            return None
        
        if key in self.map:
            updated_node = self.map[key]
            updated_node.value = value
            self._move_to_head(updated_node)
        else:
            node = Node(key, value)
            self._prepend_to_head(node)

            
        if len(self.map) > self.capacity:
            self._remove_lru()
            