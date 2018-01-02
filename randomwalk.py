import random
import matplotlib.pyplot as plt


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
        return (self.x ** 2 + self.x ** 2) ** 0.5


class Drunk:

    def __init__(self, x=0, y=0):
        self.location = Vector(x, y)

    def __repr__(self):
        return '<Drunk: {}>'.format(self.location)

    def take_step(self):
        possible_movements = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        possible_vectors = [Vector(x, y) for x, y in possible_movements]
        self.location += random.choice(possible_vectors)


class Field:

    def __init__(self):
        self.drunks = []

    def add_drunk(self, drunk):
        self.drunks.append(drunk)

    def move_drunks(self):
        for drunk in self.drunks:
            drunk.take_step()


class FieldPlotter:

    @staticmethod
    def plot(field, steps):
        plt.figure(1)
        positions = []
        for i in range(steps):
            for drunk in field.drunks:
                d_location = drunk.location
                positions.append((d_location.x, d_location.y))
            field.move_drunks()
        x, y = zip(*positions)
        plt.plot(x, y)
        plt.show()
