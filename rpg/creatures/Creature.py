__author__ = 'winniehell'

import copy


class ActionWrapper(dict):
    def __init__(self, executor):
        super().__init__()
        self._executor = executor

    def add(self, action):
        self[repr(action)] = lambda target: (action(executor=self._executor, target=target))

    def __getattr__(self, key):
        return self[key]


class Creature:

    def __init__(self, name: str, stats: dict):
        """
        stats can not drop below 0 and can not exceed their initial value.
        """
        self._name = name
        self._initial_stats = stats
        self._stats = copy.deepcopy(stats)

        self._actions = ActionWrapper(self)
        self._items = list()

    def __repr__(self):
        return '{name} ({stats}) [{actions}]'.format(
            name=self._name,
            stats=', '.join(
                '{0}: {1}'.format(name.capitalize(), self._stats[name])
                for name
                in sorted(self._stats.keys())
            ),
            actions=', '.join(
                action.capitalize()
                for action
                in self._actions.keys()
            )
        )

    def is_alive(self):
        return self.hitpoints > 0

    def __getattr__(self, key):
        if key in ('name', 'actions', 'items'):
            return self.__dict__['_'+key]

        return self._stats[key]

    def __setattr__(self, key: str, value):
        if key.startswith('_'):
            self.__dict__[key] = value
            return

        if key in self._stats:
            self._stats[key] = max(0, min(value, self._initial_stats[key]))
        else:
            raise KeyError(key)
