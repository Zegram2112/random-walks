from randomwalk import Field, Drunk, WalkAnalysis
from sys import argv
from timeit import timeit

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
        analysis = WalkAnalysis(sim_results)
        analysis.plot_paths()
        analysis.show_plots()
    elif "timeit" in argv:
        s = "from randomwalk import Field, Drunk, WalkAnalysis, Vector"
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
        timedrunk("an.abs_results")
        timedrunk("an.means")
        timedrunk("an.stdevs")
        timedrunk("an.plot_paths()")
        timedrunk("an.plot_distances()")
        timedrunk("f.sim_walks(1000, 1000)")
