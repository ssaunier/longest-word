# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import random
import requests

class Game:
    GRID_SIZE = 9

    def __init__(self):
        self.grid = []
        for _ in range(self.GRID_SIZE):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False

        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)

    def __check_dictionary(self, word):
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = r.json()
        return response['found']
