class UndergroundSystem:

    def __init__(self):
        self.id = {}
        self.ins = defaultdict(int)
        self.count = defaultdict(int)


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id[id] = (stationName, t)
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        n2, t2 = self.id.pop(id)
        self.ins[n2, stationName] += t - t2
        self.count[n2, stationName] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.ins[startStation, endStation]/self.count[startStation, endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)