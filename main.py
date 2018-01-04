from randomwalk import Field, Drunk, SimAnalizer
from sys import argv
from timeit import timeit

if __name__ == '__main__':
    if "examples" in argv:
        f = Field()
        f.add_drunk(Drunk())
        f.add_drunk(Drunk())
        f.add_drunk(Drunk())
        sim_results = f.simulate(10000)
        SimAnalizer.plot_paths(sim_results)
        SimAnalizer.plot_distances(sim_results)
    elif "timeit" in argv:
        s = "from randomwalk import Field, Drunk, SimAnalizer, Vector"
        s += "\nf = Field()"
        s += "\nd = Drunk()"
        s += "\nf.add_drunk(d)"
        def timedrunk(sentence):
            print(sentence)
            print(timeit(sentence, setup=s, number=1))
            print("-" * 40)
        timedrunk("d.take_step()")
        timedrunk("f.simulate(100000)")
        timedrunk("SimAnalizer.plot_paths(f.simulate(100000))")
        timedrunk("SimAnalizer.plot_distances(f.simulate(100000))")
