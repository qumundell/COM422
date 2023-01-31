import pytest
from car import Car


def test_create_car():
    c1 = Car(30, 100, 70)
    assert c1.fuelLevel == 70


def test_accelerate_to_max():
    c1 = Car(50, 100, 70)
    c1.accelerate(60)
    assert c1.currentSpeed == 100


def test_accelerate_fuel_zero():
    c1 = Car(50, 100, 30)
    c1.accelerate(40)
    assert c1.fuelLevel == 0


def test_accelerate_fuel_zero_speed():
    c1 = Car(50, 100, 30)
    c1.accelerate(40)
    assert c1.currentSpeed == 0


def test_accelerate_at_max():
    c1 = Car(100, 100, 50)
    c1.accelerate(20)
    assert c1.currentSpeed == 100

