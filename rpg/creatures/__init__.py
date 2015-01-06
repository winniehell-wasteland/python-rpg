__author__ = 'winniehell'

import importlib
import json

from creatures.Creature import Creature


def load(file_name: str) -> list:

    loaded_creatures = list()

    with open(file_name) as creatures_file:
        for player_data in json.load(creatures_file):
            actions = list()

            for action_data in player_data.pop('actions', list()):
                action_type = action_data.pop('type').capitalize()
                action_class = getattr(importlib.import_module('actions.'+action_type), action_type)
                actions.append(action_class(**action_data))

            creature = Creature(actions=actions, **player_data)

            loaded_creatures.append(creature)

    return loaded_creatures
