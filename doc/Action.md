# Creating an action
    >>> from rpg.actions.Attack import Attack

    >>> tackle = Attack(name='Tackle', stat='strength', difficulty=25, damage_range=(10,10))
    >>> print(tackle)
    Tackle

# Executing an action
    >>> from rpg.creatures import Creature
    >>> somebody = Creature(name='Somebody', stats={'strength': 30})
    >>> anybody = Creature(name='Anybody', stats={'hitpoints' : 100})

    >>> somebody.actions.add(tackle)
    >>> somebody.actions.tackle(anybody)
    >>> print(anybody.hitpoints)
    90

    >>> somebody.strength = 0
    >>> somebody.actions.tackle(anybody)
    >>> print(anybody.hitpoints)
    90
