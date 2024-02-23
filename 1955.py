class SeatManager:

    def __init__(self, n: int):
        self.n = n
        #self.h = defaultdict()
        self.a = [i for i in range(1, n+1)]
        heapify(self.a)

    def reserve(self) -> int:
        s = heappop(self.a)
        #self.h[s] = True
        return s

    def unreserve(self, seatNumber: int) -> None:
        #self.h[seatNumber] = False
        heappush(self.a, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)