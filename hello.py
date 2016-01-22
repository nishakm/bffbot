import random


class Hello:
    """Class containing all the different ways of saying Hello"""

    def __init__(self):
        self.hellos = ['hello', 'hi', 'hey', 'yo', 'howdy', 'sup']

    def get_hello(self):
        index = random.randrange(0, len(self.hellos))
        return self.hellos[index]

    def say_it(self):
        print self.get_hello()

    def greet(self):
        print "Hi! I'm bffbot"
        print "What's up?"
