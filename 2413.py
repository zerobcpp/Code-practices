class SmallestInfiniteSet1:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.map = {i : 1 for i in self.heap}
    

    def popSmallest(self) -> int:
        if self.heap:
            idx = heapq.heappop(self.heap)
            del self.map[idx]
            return idx
        return -1
        

    def addBack(self, num: int) -> None:
        if num not in self.map:
            self.map[num] = 1
            heapq.heappush(self.heap, num)
            
            
class SmallestInfiniteSet:

    def __init__(self):
        self.n = 1
        self.seen = set()
        self.heap = []
    

    def popSmallest(self) -> int:
        if self.heap:
            res = heappop(self.heap)
            self.seen.remove(res)
        else:
            res = self.n
            self.n += 1
        return res
        

    def addBack(self, num: int) -> None:
        if num not in self.seen and num < self.n:
            self.seen.add(num)
            heappush(self.heap, num)
        
        
        
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)