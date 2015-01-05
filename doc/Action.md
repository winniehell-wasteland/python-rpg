# Creating an action
    >>> from rpg.creatures import Creature
    >>> somebody = Creature(name='Somebody', stats={'strength': 30})

    >>> from rpg.actions.Attack import Attack

    >>> tackle = Attack(creature=somebody, name='Tackle', stat='strength', difficulty=25, damage_range=(10,10))
    >>> print(tackle)
    Somebody: Tackle

# Executing an action
    >>> anybody = Creature(name='Anybody', stats={'hitpoints' : 100})

    >>> tackle.execute(target=anybody)
    >>> print(anybody.stats['hitpoints'])
    90

    >>> somebody.stats['strength'] = 0
    >>> tackle.execute(target=anybody)
    >>> print(anybody.stats['hitpoints'])
    90
