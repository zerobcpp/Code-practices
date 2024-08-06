class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 256
        self.table = [None] * self.size


    def add(self, key):
        b = key % self.size
        if self.table[b] == None:
            self.table[b] = [key]
        else:
            self.table[b].append(key)

    def remove(self, key):
        b = key % self.size
        if self.table[b]:
            while key in self.table[b]: 
                self.table[b].remove(key)
                
    def contains(self,key):
        b = key % self.size
        if self.table[b] != None:
            return key in self.table[b]
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)