# Creating an item
    >>> from rpg.items.Potion import Potion

    >>> potion = Potion(hitpoints=20)
    >>> print(potion)
    Potion (Hitpoints: 20)

# Using an item
    >>> from rpg.creatures import Creature
    >>> somebody = Creature(name='Somebody', stats={'hitpoints': 100})
    >>> somebody.change_stat(name='hitpoints', value=-20)

    >>> potion.use(target=somebody)
    >>> print(somebody.stats['hitpoints'])
    100
