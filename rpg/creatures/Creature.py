import copy

__author__ = 'winniehell'


class Creature:
    def __init__(self, name: str, stats: dict):
        self.name = name
        self.initial_stats = stats
        self.stats = copy.deepcopy(stats)
        self.actions = list()
        self.items = list()

    def __repr__(self):
        return '{name} ({stats}) [{actions}]'.format(
            name=self.name,
            stats=', '.join(
                '{0}: {1}'.format(name.capitalize(), self.stats[name])
                for name
                in sorted(self.stats.keys())
            ),
            actions=', '.join(
                action.name
                for action
                in self.actions
            )
        )

    def change_stat(self, name: str, value: int):
        """
        stats can not drop below 0 and can not exceed their initial value.
        @param name:
        @param value:
        @return:
        """
        self.stats[name] = max(0, min(self.stats[name] + value, self.initial_stats[name]))

    def is_alive(self):
        return self.stats['hitpoints'] > 0
