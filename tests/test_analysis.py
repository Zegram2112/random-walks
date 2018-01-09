import unittest
from randomwalk.core import Drunk, Field, Vector
from randomwalk.analysis import WalkAnalysis
import numpy as np

class WalkAnalysisTestCase(unittest.TestCase):

    def setUp(self):
        self.d1 = Drunk(1, 1)
        self.d2 = Drunk(0, -2)
        self.walk_results = {
            self.d1: np.array([Vector(0, 0), Vector(1, 0), Vector(1, 1)]),
            self.d2: np.array([Vector(0, 0), Vector(0, -1), Vector(0, -2)]),
        }
        self.abs_results = {
            self.d1: np.array([0, 1, (2)**0.5]),
            self.d2: np.array([0, 1, 2]),
        }
        self.analysis = WalkAnalysis(self.walk_results)

    def test_abs_results(self):
        abs_distances = self.analysis.abs_results
        self.assertTrue(
            np.array_equal(
                abs_distances[self.d1],
                self.abs_results[self.d1]
            )
        )

    def test_means(self):
        means = self.analysis.means
        self.assertAlmostEqual(
            means[self.d1], (1 + (2)**0.5) / 3
        )

    def test_stdevs(self):
        stdevs = self.analysis.stdevs
        mean = (1 + (2) ** 0.5) / 3
        self.assertAlmostEqual(
            stdevs[self.d1],
            np.std(self.abs_results[self.d1])
        )
