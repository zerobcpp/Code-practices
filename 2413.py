class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.map = {i : 1 for i in self.heap}
    

    def popSmallest(self) -> int:
        if self.heap:
            idx = heapq.heappop(self.heap)
            del self.map[idx]
            return idx
        return 
        

    def addBack(self, num: int) -> None:
        if num not in self.map:
            self.map[num] = 1
            heapq.heappush(self.heap, num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)