#!/usr/bin/env python3

class Dog:
    """A simple model"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simiulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

my_dog = Dog('Cezar', 10)
print(f"My dog name was {my_dog.name}")

my_dog.sit()
