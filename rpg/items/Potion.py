from creatures import Creature

__author__ = 'winniehell'


class Potion:
    def __init__(self, hitpoints: int):
        self.hitpoints = hitpoints

    def use(self, target: Creature):
        target.change_stat(name='hitpoints', value=+self.hitpoints)

    def __repr__(self):
        return '{name} (Hitpoints: {hitpoints})'.format(name=type(self).__name__, hitpoints=self.hitpoints)
