from Dog import Dog
from Enclosure import Enclosure
from Kennel_Company import Kennel_Company
import pytest


def load_enclosures_stub(self):
    return [Enclosure(1,100,2)]


def check_suitability_stub(self, dog):
    return True


def remove_dog_stub(self, name):
    self.enclosures[0].remove_occupant(name)


def add_occupant_stub(self, dog):
    self.occupants.append(dog)


def test_book_dog(monkeypatch):
    # Create a kennel company
    monkeypatch.setattr(Kennel_Company, 'load_enclosures', load_enclosures_stub)
    monkeypatch.setattr(Enclosure, "check_suitability", check_suitability_stub)
    monkeypatch.setattr(Enclosure, "add_occupant", add_occupant_stub)

    k_comp = Kennel_Company()
    # Book 2 dogs in to the kennels
    d1 = Dog("Spot", "Spicko", 5, "Daschund", "Has a big nose")
    d2 = Dog("Bill", "Bricko", 4, "Big dog", "is big")
    k_comp.book_dog(d1)
    k_comp.book_dog(d2)
    # Check that the overall number of spaces left in the kennels is correct after the 2 bookings
    assert k_comp.spaces_left() == 0


def test_remove_dog(monkeypatch):
    # Create a kennel company
    monkeypatch.setattr(Kennel_Company, 'load_enclosures', load_enclosures_stub)
    monkeypatch.setattr(Enclosure, "check_suitability", check_suitability_stub)
    monkeypatch.setattr(Enclosure, "add_occupant", add_occupant_stub)
    monkeypatch.setattr(Kennel_Company, 'remove_dog', remove_dog_stub)

    k_comp = Kennel_Company()
    # The kennel company will need to have at least 1 dog staying with it - facilitate this
    k_comp.book_dog(Dog("Paul", "Poul", 13, "Daschund", "Big dog"))
    # Remove the dog
    k_comp.remove_dog("Paul")
    # Check that the overall number of spaces left is correct after the removal
    assert k_comp.spaces_left() == 0
