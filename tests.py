import unittest
from randomwalk import Vector, Drunk, Field


class VectorTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Vector(1, 1) + Vector(-2, 2),
                         Vector(-1, 3))

    def test_equality(self):
        self.assertEqual(Vector(1, 1), Vector(1, 1))

    def test_repr(self):
        self.assertEqual(
            repr(Vector(1, 1)), '<Vector: (1, 1)>'
        )

    def test_str(self):
        self.assertEqual(
            str(Vector(1, 1)), '(1, 1)'
        )

    def test_multiplication(self):
        self.assertEqual(
            Vector(1, -2) * 2, Vector(2, -4)
        )

    def test_r_multiplication(self):
        self.assertEqual(
            2 * Vector(1, -2), Vector(2, -4)
        )

    def test_substraction(self):
        self.assertEqual(
            Vector(1, 1) - Vector(1, -2), Vector(0, 3)
        )

    def test_absolute(self):
        self.assertEqual(
            abs(Vector(2, 2)), 2 * (2) ** 0.5
        )

    def test_default_value(self):
        self.assertEqual(
            Vector(), Vector(0, 0)
        )


class DrunkTestCase(unittest.TestCase):

    def setUp(self):
        self.drunk = Drunk()

    def test_repr(self):
        self.assertEqual(
            repr(Drunk(1, 1)), '<Drunk: (1, 1)>'
        )

    def test_default_cero(self):
        self.assertEqual(
            Drunk().location, Vector(0, 0)
        )

    def test_take_step(self):
        admited_values = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        admited_vectors = [Vector(x, y) for x, y in admited_values]
        for i in range(1000):
            self.drunk.location = Vector()
            self.drunk.take_step()
            if self.drunk.location not in admited_vectors:
                self.fail(
                    "Drunk outside admited value: {}".format(
                    self.drunk.location
                    )
                )


class FieldTestCase(unittest.TestCase):

    def test_move_drunks(self):
        d1 = Drunk()
        d2 = Drunk(1, 1)
        f = Field()
        f.add_drunk(d1)
        f.add_drunk(d2)
        v1, v2 = d1.location, d2.location
        f.move_drunks()
        if d1.location == v1 or d2.location == v2:
            self.fail()


if __name__ == '__main__':
    unittest.main()
