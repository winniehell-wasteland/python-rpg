__author__ = 'winniehell'


class Potion:
    def __init__(self, hitpoints: int):
        self.hitpoints = hitpoints

    def use(self, target):
        target.hitpoints += self.hitpoints

    def __repr__(self):
        return '{name} (Hitpoints: {hitpoints})'.format(name=type(self).__name__, hitpoints=self.hitpoints)
