class MyHashMap:

    def __init__(self):
        self.hash = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        k = hash(key)
        self.hash[k] = value
        

    def get(self, key: int) -> int:
        k = hash(key)
        if self.hash[k] != None:
            return self.hash[k]
        return -1
        

    def remove(self, key: int) -> None:
        k = hash(key)
        self.hash[k] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)