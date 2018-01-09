import unittest
from randomwalk.core import Vector, Drunk, Field
from randomwalk.analysis import WalkAnalysis
import numpy as np


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

    def test_tuple_conversion(self):
        self.assertEqual(
            tuple(Vector(1, -2)), (1, -2)
        )

    def test_array(self):
        self.assertTrue(
            np.array_equal(
                Vector(1, 2).array(), np.array([1, 2])
            )
        )


class DrunkTestCase(unittest.TestCase):

    def setUp(self):
        self.drunk = Drunk()

    def test_repr(self):
        self.assertEqual(
            repr(self.drunk), '<Drunk {}: (0, 0)>'.format(
                self.drunk.id
            )
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

    def test_automatic_id(self):
        self.assertNotEqual(Drunk().id, Drunk().id)


class FieldTestCase(unittest.TestCase):

    def setUp(self):
        self.d1 = Drunk()
        self.d2 = Drunk(1, 1)
        self.f = Field()
        self.f.add_drunk(self.d1)
        self.f.add_drunk(self.d2)

    def test_move_drunks(self):
        v1, v2 = self.d1.location, self.d2.location
        self.f.move_drunks()
        if self.d1.location == v1 or self.d2.location == v2:
            self.fail()

    def test_walk_results(self):
        results = self.f.walk(1)
        self.assertTrue(self.d1 in results)
        self.assertTrue(self.d2 in results)
        self.assertEqual(
            type(results[self.d1][0]), Vector
        )
        self.assertNotEqual(
            results[self.d1][1], Vector(0, 0)
        )

    def test_reset(self):
        self.f.move_drunks()
        self.f.reset()
        self.assertEqual(
            self.d1.location, Vector(0, 0)
        )

    def test_sim_results(self):
        results = self.f.sim_walks(10, 100)
        self.assertTrue(
            isinstance(results[self.d1][0], Vector)
        )
