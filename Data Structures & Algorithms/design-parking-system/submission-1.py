class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.space = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.space[carType-1] > 0:
            self.space[carType-1] -= 1
            return True
        return False
        
