from car import Car


def run():
    c1 = Car(0, 150, 100)
    c2 = Car(0, 200, 100)
    print(c1)
    print(c2)
    c1.accelerate(80)
    c2.brake(10)
    print(c1)
    print(c2)
    c1.refuel(80)
    c1.accelerate(75)
    print(c1)
    print(c2)


run()
