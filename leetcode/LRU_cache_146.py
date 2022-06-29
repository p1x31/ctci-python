class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node
        # head and tail are dummy nodes left =LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    #remove least recently used node
    def remove(self, node):
        nxt = node.next #get next node
        prev = node.prev # get prev node
        prev.next, nxt.prev = nxt, prev #point to next node two pointers
        
    #at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right # get pointers from prev and nxt node
        prev.next, nxt.prev = node, node # connect to neighbour
        node.next, node.prev = nxt, prev # point right and prev at the inserted node
       

    #update moset recently used node
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:#node already exists
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)