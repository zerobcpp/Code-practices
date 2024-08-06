class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.map = {}
        self.map[3] = small
        self.map[2] = medium
        self.map[1] = big

    def addCar(self, carType: int) -> bool:
        if self.map[carType] > 0:
            self.map[carType] -= 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)