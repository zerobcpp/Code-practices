class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.c = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        
        if key in self.c:
            node = self.c[key]
            print(node.k)
            self.rmv(node)
            self.ins(node)
            return node.v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        n = Node(key, value)
        if key in self.c:
            self.rmv(self.c[key])
        self.c[key] = n
        self.ins(n)
        
        while len(self.c) > self.n:
            r_node = self.tail.prev
            self.rmv(r_node)
            del self.c[r_node.k]
        
    
    def ins(self, node):
        cur = self.head.next
        cur.prev = node
        node.next = cur
        node.prev = self.head
        self.head.next = node
        #self.debug()
        
    def rmv(self, node):
        prev = node.prev
        n = node.next
        prev.next = n
        n.prev = prev
        
    def debug(self):
        cur = self.head
        while cur:
            print('[', cur.k, cur.v, ']', end = '->')
            cur = cur.next
        print('\n')

    
    
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)