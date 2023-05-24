#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition="New"):
        self.brand = brand
        self.size = size
        self.condition = condition

    def set_size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            print("size must be an integer")
    size = property(None, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"