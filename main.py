from randomwalk.core import Field, Drunk
from randomwalk.analysis import WalkAnalysis, SimAnalysis
from sys import argv
from timeit import timeit
from tests import test_core, test_analysis
import unittest

if __name__ == '__main__':
    if "examples" in argv:
        f = Field()
        f.add_drunk(Drunk())
        f.add_drunk(Drunk())
        f.add_drunk(Drunk())
        walk_results = f.walk(10000)
        analysis = WalkAnalysis(walk_results)
        analysis.plot_paths()
        analysis.plot_distances()
        analysis.show_plots()
        sim_results = f.sim_walks(1000, 100)
        analysis = SimAnalysis(sim_results)
        analysis.plot_positions()
        analysis.show_plots()
    elif "timeit" in argv:
        s = "from randomwalk.core import Field, Drunk, Vector"
        s += "\nfrom randomwalk.analysis import WalkAnalysis"
        s += "\nf = Field()"
        s += "\nd = Drunk()"
        s += "\nf.add_drunk(d)"
        s += "\nsim = f.walk(10000)"
        s += "\nan = WalkAnalysis(sim)"
        print(s)
        def timedrunk(sentence):
            print(sentence)
            print(timeit(sentence, setup=s, number=1))
            print("-" * 40)
        timedrunk("d.take_step()")
        timedrunk("f.walk(1000)")
        timedrunk("an.distances")
        timedrunk("an.means")
        timedrunk("an.stdevs")
        timedrunk("an.plot_paths()")
        timedrunk("an.plot_distances()")
        timedrunk("f.sim_walks(1000, 1000)")
    elif "test" in argv:
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTests(loader.loadTestsFromModule(test_core))
        suite.addTests(loader.loadTestsFromModule(test_analysis))
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
