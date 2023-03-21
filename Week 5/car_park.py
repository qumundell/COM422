from car import Car
class CarPark:
    def __init__(self, capacity):
        self.capacity = capacity
        self.occupants = []

    def is_full(self):
        if len(self.occupants) == self.capacity:
            return True
        else:
            return False

    def remove_vehicle(self, name):
        found = False
        for i in range(len(self.occupants)):
            if self.occupants[i].reg == name:
                self.occupants[i] = None
                found = True
        if found is False:
            print(f"Could not find the car {name}")

    def add_vehicle(self, car):
        added = False
        if car is not Car:
            return False
        for i in range(len(self.occupants)):
            if self.occupants[i] is None:
                self.occupants[i] = car
                added = True
        if added is False:
            if self.is_full() is True:
                print("The car park is currently full, my apologies")
            else:
                self.occupants.append(car)

    def spaces_available(self):
        count = 0
        for i in range(len(self.occupants)):
            if self.occupants[i] is None:
                count += 1
        count += self.capacity - len(self.occupants)
        return count
