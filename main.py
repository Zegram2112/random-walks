from randomwalk import Field, Drunk, WalkAnalizer
from sys import argv
from timeit import timeit

if __name__ == '__main__':
    if "examples" in argv:
        f = Field()
        f.add_drunk(Drunk())
        f.add_drunk(Drunk())
        f.add_drunk(Drunk())
        walk_results = f.walk(10000)
        WalkAnalizer.plot_paths(walk_results)
        WalkAnalizer.plot_distances(walk_results)
        WalkAnalizer.show_plots()
        sim_results = f.sim_walks(1000, 100)
        WalkAnalizer.plot_paths(sim_results)
        WalkAnalizer.show_plots()
    elif "timeit" in argv:
        s = "from randomwalk import Field, Drunk, WalkAnalizer, Vector"
        s += "\nf = Field()"
        s += "\nd = Drunk()"
        s += "\nf.add_drunk(d)"
        s += "\nsim = f.walk(10000)"
        s += "\nabs = WalkAnalizer.abs_results(sim)"
        print(s)
        def timedrunk(sentence):
            print(sentence)
            print(timeit(sentence, setup=s, number=1))
            print("-" * 40)
        timedrunk("d.take_step()")
        timedrunk("f.walk(100000)")
        timedrunk("WalkAnalizer.abs_results(sim)")
        timedrunk("WalkAnalizer.means(abs)")
        timedrunk("WalkAnalizer.stdevs(abs)")
        timedrunk("WalkAnalizer.plot_paths(sim)")
        timedrunk("WalkAnalizer.plot_distances(sim)")
        timedrunk("f.sim_walks(1000, 1000)")
