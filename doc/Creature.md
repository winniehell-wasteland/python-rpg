# Creating of a creature
    >>> from rpg.creatures import Creature
    >>> somebody = Creature(name='Somebody', stats={})
    >>> print(somebody)
    Somebody () []

# Creating of a creature with statistics
    >>> anybody = Creature(name='Anybody', stats={'hitpoints': 100, 'endurance': 7})
    >>> print(anybody)
    Anybody (Endurance: 7, Hitpoints: 100) []

# Changing the stats of a creature
    >>> anybody.change_stat(name='hitpoints', value=-20)
    >>> print(anybody.stats['hitpoints'])
    80

    >>> anybody.change_stat(name='hitpoints', value=+40)
    >>> print(anybody.stats['hitpoints'])
    100

    >>> anybody.change_stat(name='hitpoints', value=-200)
    >>> print(anybody.stats['hitpoints'])
    0

    >>> anybody.change_stat(name='strength', value=-5)
    Traceback (most recent call last):
        ...
    KeyError: 'strength'

# Checking whether a creature is still alive
    >>> anybody.stats['hitpoints'] = 50
    >>> print(anybody.is_alive())
    True

    >>> anybody.stats['hitpoints'] = 0
    >>> print(anybody.is_alive())
    False
