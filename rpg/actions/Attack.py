import random

from creatures import Creature


__author__ = 'winniehell'


class Attack:
    def __init__(self, creature: Creature, name: str, stat: str, difficulty: int, damage_range: tuple):
        self.creature = creature
        self.name = name
        self.stat = stat
        self.difficulty = int(difficulty)
        assert len(damage_range) == 2
        self.damage_range = damage_range

    def execute(self, target : Creature):
        attack_dice = random.randint(0, 20)
        is_hitting = (attack_dice + self.creature.stats[self.stat]) > self.difficulty

        if not is_hitting:
            return

        if attack_dice == 20:
            damage = max(*self.damage_range)
        else:
            damage = random.randint(*self.damage_range)

        target.change_stat('hitpoints', -damage)

    def __repr__(self):
        return '{creature}: {name}'.format(
            creature=self.creature.name,
            name=self.name
        )
