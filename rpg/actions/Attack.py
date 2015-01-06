__author__ = 'winniehell'

import random


class Attack:
    def __init__(self, name: str, stat: str, difficulty: int, damage_range: tuple):
        self._name = name
        self._stat = stat
        self._difficulty = int(difficulty)
        assert len(damage_range) == 2
        self._damage_range = damage_range

    def __call__(self, executor, target):
        attack_dice = random.randint(0, 20)
        is_hitting = (attack_dice + getattr(executor, self._stat)) > self._difficulty

        if not is_hitting:
            return

        if attack_dice == 20:
            damage = max(*self._damage_range)
        else:
            damage = random.randint(*self._damage_range)

        target.hitpoints -= damage

    def __repr__(self):
        return self._name.lower()

    def __str__(self):
        return self._name
