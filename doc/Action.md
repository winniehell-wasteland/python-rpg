# Creating an action
    >>> from rpg.actions.Attack import Attack

    >>> tackle = Attack(name='Tackle', stat='strength', difficulty=25, damage_range=(10,10))
    >>> print(tackle)
    Tackle

# Executing an action
    >>> from rpg.creatures import Creature
    >>> somebody = Creature(name='Somebody', stats={'strength': 30}, actions=[tackle])
    >>> anybody = Creature(name='Anybody', stats={'hitpoints' : 100}, actions=[])

    >>> somebody.actions['Tackle'].execute(target=anybody)
    >>> print(anybody.hitpoints)
    90

    >>> somebody.strength = 0
    >>> somebody.actions['Tackle'].execute(target=anybody)
    >>> print(anybody.hitpoints)
    90
