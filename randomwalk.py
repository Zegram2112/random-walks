import random
import matplotlib.pyplot as plt
from statistics import mean, stdev


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return '<Vector: ({}, {})>'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + (-1 * other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __iter__(self):
        return iter((self.x, self.y))


class Drunk:

    next_id = 0

    def __init__(self, x=0, y=0, possible_movements=None):
        self.id = Drunk.next_id
        self.location = Vector(x, y)
        if possible_movements is None:
            self.possible_movements = [
                Vector(x, y) for x, y in [
                        (-1, 0), (1, 0), (0, 1), (0, -1)
                    ]
                ]
        else:
            self.possible_movements = [
                Vector(x, y) for x, y in possible_movements
            ]
        Drunk.next_id += 1

    def __repr__(self):
        return '<Drunk {}: {}>'.format(self.id, self.location)

    def take_step(self):
        self.location += random.choice(self.possible_movements)


class Field:

    def __init__(self):
        self.drunks = []
        self.initial_locations = {}

    def add_drunk(self, drunk):
        self.drunks.append(drunk)
        self.initial_locations[drunk] = drunk.location

    def move_drunks(self):
        for drunk in self.drunks:
            drunk.take_step()

    def simulate(self, steps):
        self.reset()
        results = {}
        for drunk in self.drunks:
            results[drunk] = [drunk.location]
        for i in range(steps):
            self.move_drunks()
            for drunk in self.drunks:
                results[drunk].append(drunk.location)
        return results

    def reset(self):
        for drunk in self.drunks:
            drunk.location = self.initial_locations[drunk]


class SimAnalizer:

    linewidth = 0.4

    @staticmethod
    def abs_results(sim_results):
        abs_distances = {}
        for drunk, positions in sim_results.items():
            abs_distances[drunk] = [abs(v) for v in positions]
        return abs_distances

    @staticmethod
    def means(abs_results):
        means = {}
        for drunk, distances in abs_results.items():
            means[drunk] = mean(distances)
        return means

    @staticmethod
    def stdevs(abs_results):
        stdevs = {}
        for drunk, distances in abs_results.items():
            stdevs[drunk] = stdev(distances)
        return stdevs

    @classmethod
    def plot_paths(cls, sim_results):
        plt.figure(1)
        abs_results = cls.abs_results(sim_results)
        means = cls.means(abs_results)
        stdevs = cls.stdevs(abs_results)
        for drunk, positions in sim_results.items():
            x, y = zip(*positions)
            name = 'Drunk {}'.format(drunk.id)
            label_str = '{}\nMean: {}\nStdev: {}'.format(
                name, round(means[drunk], 2), round(stdevs[drunk], 2)
            )
            plt.plot(x, y, label=label_str, linewidth=cls.linewidth)
        plt.legend()
        plt.show()

    @classmethod
    def plot_distances(cls, sim_results):
        plt.figure(2)
        abs_results = cls.abs_results(sim_results)
        means = cls.means(abs_results)
        stdevs = cls.stdevs(abs_results)
        for drunk, distances in abs_results.items():
            x = list(range(len(distances)))
            y = distances
            name = 'Drunk {}'.format(drunk.id)
            label_str = '{}\nMean: {}\nStdev: {}'.format(
                name, round(means[drunk], 2), round(stdevs[drunk], 2)
            )
            plt.plot(x, y, label=label_str, linewidth=cls.linewidth)
        plt.legend()
        plt.show()
