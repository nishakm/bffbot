import random


class Goodbye:
    """Class containing all the different ways of signing off"""

    def __init__(self):
        self.goodbyes = ['goodbye',
                         'bye',
                         'see ya',
                         'adios',
                         'hasta',
                         'later',
                         'byeeee']

    def get_goodbye(self):
        index = random.randrange(0, len(self.goodbyes))
        return self.goodbyes[index]

    def say_it(self):
        print self.get_goodbye()
