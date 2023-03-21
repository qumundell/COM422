class Car:
    def __init__(self, regno, maxSpeed, fuelLevel=100, currentSpeed=0):
        self.reg = regno
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel
        self.currentSpeed = currentSpeed

    def accelerate(self, amount):
        for i in range(amount):
            if self.currentSpeed == self.maxSpeed:
                print("WE'VE REACHED MAXIMUM SPEED")
                return
            elif self.fuelLevel == 0:
                print("WE'RE OUT OF FUEL")
                self.currentSpeed = 0
                return
            self.currentSpeed += 1
            self.fuelLevel -= 1

    def brake(self, amount):
        for i in range(amount):
            if self.currentSpeed == 0:
                print("We have reached a halt")
                return
            self.currentSpeed -= 1

    def refuel(self, amount):
        for i in range(amount):
            if self.fuelLevel == 100:
                print("We are at full capacity")
                return
            self.fuelLevel += 1

    def __str__(self):
        return f"Current Speed: {self.currentSpeed}, Max Speed: {self.maxSpeed}, Fuel Level: {self.fuelLevel}"
