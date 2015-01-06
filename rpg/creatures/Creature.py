__author__ = 'winniehell'

import copy


class ActionWrapper:
    def __init__(self, executor, action):
        self._executor = executor
        self._action = action

    def execute(self, target):
        self._action.execute(executor=self._executor, target=target)

    def __repr__(self):
        return repr(self._action)

class Creature:

    def __init__(self, name: str, stats: dict, actions):
        """
        stats can not drop below 0 and can not exceed their initial value.
        """
        self._name = name
        self._initial_stats = stats
        self._stats = copy.deepcopy(stats)

        self._actions = dict(
            (repr(action), ActionWrapper(executor=self, action=action))
            for action
            in actions
        )

    def __repr__(self):
        return '{name} ({properties})'.format(
            name=self._name,
            properties=', '.join(
                [
                    '{0}: {1}'.format(name.capitalize(), self._stats[name])
                    for name
                    in sorted(self._stats.keys())
                ] +
                [
                    'Actions: [{actions}]'.format(actions=', '.join(sorted(self._actions.keys())))
                ]

            )
        )

    def is_alive(self):
        return self.hitpoints > 0

    def __getattr__(self, key):
        if key in ('name', 'actions'):
            return self.__dict__['_'+key]

        return self._stats[key]

    def __setattr__(self, key: str, value):
        if key.startswith('_'):
            self.__dict__[key] = value
        elif key in self._stats:
            self._stats[key] = max(0, min(value, self._initial_stats[key]))
        else:
            raise AttributeError(key)
