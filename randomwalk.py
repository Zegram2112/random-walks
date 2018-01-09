import random
import matplotlib.pyplot as plt
import numpy as np


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

    def array(self):
        return np.array([self.x, self.y])


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

    def walk(self, steps):
        self.reset()
        results = {}
        for drunk in self.drunks:
            results[drunk] = [drunk.location]
        for i in range(steps):
            self.move_drunks()
            for drunk in self.drunks:
                results[drunk].append(drunk.location)
        for drunk in results:
            results[drunk] = np.array(results[drunk])
        return results

    def sim_walks(self, walks, steps):
        sim_results = {}
        for drunk in self.drunks:
            sim_results[drunk] = []
        for i in range(walks):
            walk_results = self.walk(steps)
            for drunk in walk_results:
                sim_results[drunk].append(
                    walk_results[drunk][-1]
                )
        for drunk in sim_results:
            sim_results[drunk] = np.array(sim_results[drunk])
        return sim_results


    def reset(self):
        for drunk in self.drunks:
            drunk.location = self.initial_locations[drunk]


class WalkAnalysis:

    linewidth = 0.4

    def __init__(self, walk_results):
        self.walk_results = walk_results
        self._abs_results = None
        self._means = None
        self._stdevs = None

    @property
    def abs_results(self):
        if self._abs_results is None:
            abs_distances = {}
            for drunk, positions in self.walk_results.items():
                abs_distances[drunk] = abs(positions)
            self._abs_results = abs_distances
            return abs_distances
        else:
            return self._abs_results

    @property
    def means(self):
        if self._means is None:
            means = {}
            for drunk, distances in self.abs_results.items():
                means[drunk] = np.mean(distances)
            self._means = means
            return means
        else:
            return self._means

    @property
    def stdevs(self):
        if self._stdevs is None:
            stdevs = {}
            for drunk, distances in self.abs_results.items():
                stdevs[drunk] = np.std(distances)
            self._stdevs = stdevs
            return stdevs
        else:
            return self._stdevs

    def plot_paths(self):
        plt.figure(1)
        for drunk, positions in self.walk_results.items():
            x, y = zip(*positions)
            name = 'Drunk {}'.format(drunk.id)
            label_str = '{}\nMean: {}\nStdev: {}'.format(
                name,
                round(self.means[drunk], 2),
                round(self.stdevs[drunk], 2)
            )
            plt.plot(x, y, label=label_str, linewidth=self.linewidth)
        plt.legend()

    def plot_distances(self):
        plt.figure(2)
        for drunk, distances in self.abs_results.items():
            x = list(range(len(distances)))
            y = distances
            name = 'Drunk {}'.format(drunk.id)
            label_str = '{}\nMean: {}\nStdev: {}'.format(
                name,
                round(self.means[drunk], 2),
                round(self.stdevs[drunk], 2)
            )
            plt.plot(x, y, label=label_str, linewidth=self.linewidth)
        plt.legend()

    def show_plots(self):
        plt.show()
