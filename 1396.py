# 1396. Design Underground System

class UndergroundSystem:

    def __init__(self):
        self.id = {}
        self.ins = Counter()
        self.count = Counter()


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id[id] = (stationName, t)
        return None

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        Name2, t2 = self.id.pop(id)
        self.ins[(Name2, stationName)] += t-t2
        self.count[(Name2, stationName)] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.ins[startStation, endStation]/self.count[startStation, endStation]
