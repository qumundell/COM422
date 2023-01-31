import pytest
from car import Car


def test_create_car():
    c1 = Car(30, 100, 70)
    assert c1.fuelLevel == 70
