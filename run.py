from pprint import pprint
import random

from rpg.creatures import load

all_players, all_monsters = [load('data/{file}.json'.format(file=file)) for file in ('players', 'monsters')]

player = random.choice(all_players)
monster = random.choice(all_monsters)

while all(creature.is_alive() for creature in (player, monster)):
    pprint(player)
    pprint(monster)

    action = random.choice(list(player.actions.values()))
    action.execute(monster)

    action = random.choice(list(monster.actions.values()))
    action.execute(player)

    print()

for creature in (player, monster):
    pprint(creature)

print()

for creature in (player, monster):
    if not creature.is_alive():
        print(creature.name + ' died!')
