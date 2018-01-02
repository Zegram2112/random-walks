from randomwalk import Field, Vector, Drunk, FieldPlotter

if __name__ == '__main__':
    f = Field()
    d = Drunk()
    f.add_drunk(d)
    FieldPlotter.plot(f, 100000)
