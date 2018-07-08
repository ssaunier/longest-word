# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import random

class Game:
    GRID_SIZE = 9

    def __init__(self):
        self.grid = []
        for _ in range(self.GRID_SIZE):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
