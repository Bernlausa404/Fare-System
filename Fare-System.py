# CS3 Pair Assessment: Fare System
# Authors: (write your full names here)
# Section: (write your section here)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for every public vehicle."""

    def __init__(self, plate_number, capacity):
        self.__plate_number = plate_number
        self.__capacity = capacity
    def get_plate_number(self):
        return self.__plate_number
    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

# TODO (Part 2): write get_capacity() and set_capacity(capacity).
# set_capacity only accepts a whole number greater than 0.
# Otherwise, print "Invalid capacity." and keep the old value. 

@abstractmethod
def compute_fare(self, distance_km):
    pass
@abstractmethod
def describe(self):
    pass
# ===== Jeepney class (Developer A) =====
lass Jeepney(Vehicle):
    """Represents a Jeepney vehicle."""

    def __init__(self, plate_number, capacity):
        super().__init__(plate_number, capacity)

    def compute_fare(self, distance_km):
        base_fare = 13.00
        additional_fare_per_km = 1.50
        if distance_km <= 4:
            return base_fare
        else:
            additional_distance = distance_km - 4
            return base_fare + (additional_distance * additional_fare_per_km)

    def describe(self):
        return f"Jeepney {self.get_plate_number()} with capacity {self.get_capacity()} passengers."
# ===== Tricycle class (Developer B) =====
# ===== Tricycle class (Developer B) =====
# ===== Test code (Part 6 only) =====
