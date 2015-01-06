__author__ = 'winniehell'

import importlib
import json

from creatures.Creature import Creature


def load(file_name: str) -> list:

    loaded_creatures = list()

    with open(file_name) as creatures_file:
        for player_data in json.load(creatures_file):
            creature_actions = player_data.pop('actions', list())

            creature = Creature(**player_data)

            for action_data in creature_actions:
                action_type = action_data.pop('type').capitalize()
                action_class = getattr(importlib.import_module('actions.'+action_type), action_type)
                creature.actions.add(action_class(**action_data))

            loaded_creatures.append(creature)

    return loaded_creatures
