from randomwalk import Field, Drunk, SimAnalizer

if __name__ == '__main__':
    f = Field()
    f.add_drunk(Drunk())
    f.add_drunk(Drunk())
    f.add_drunk(Drunk())
    SimAnalizer.plot_path(f.simulate(10000))
