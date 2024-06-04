import random
import string
import requests


class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        # return True
        return self.__check_dictionary(word)

    # In Python, a @staticmethod decorator is used to define a static method within a class.
    # A static method is a method that belongs to the class rather than an instance of the class.
    # It does not require access to the instance (self) or class (cls) itself, which means it cannot modify the state of the instance or class.

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']
