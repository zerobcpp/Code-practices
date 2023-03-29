class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.table = [None] * self.size

    def hash(self,key):
        return key % self.size

    def add(self, key):
        b = key % self.size
        if self.table[b] == None:
            self.table[b] = [key]
        else:
            self.table[b].append(key)

    def remove(self, key):
        b = key % self.size
        if self.table[b] != None:
            self.table[b] = None

    def contains(self,key):
        b = key % self.size
        if self.table[b] != None:
            return key in self.table[b]
        return False

if __name__ == "__main__":
    myHashSet = MyHashSet();
    myHashSet.add(1);
    myHashSet.add(2);
    #myHashSet.showall()
    myHashSet.contains(1);
    myHashSet.contains(3);
    myHashSet.add(2);
   # myHashSet.showall()
    myHashSet.contains(2);
    myHashSet.remove(2);
    #myHashSet.showall()
    myHashSet.contains(2);
