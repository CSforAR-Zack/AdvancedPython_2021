from random import randint

class Die:
    """ A class for a single die. """

    def __init__(self, numSides=6):
        self.numSides = numSides

    def roll(self):
        """ Return a random value from 1 to numSides. """

        return randint(1, self.numSides)