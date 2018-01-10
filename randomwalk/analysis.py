import matplotlib.pyplot as plt
import numpy as np


class Analysis:

    def __init__(self, results):
        self.positions = results
        self._distances = None
        self._means = None
        self._stdevs = None

    @property
    def distances(self):
        if self._distances is None:
            distances = {}
            for drunk, positions in self.positions.items():
                distances[drunk] = abs(positions)
            self._distances = distances
            return distances
        else:
            return self._distances

    @property
    def means(self):
        if self._means is None:
            means = {}
            for drunk, distances in self.distances.items():
                means[drunk] = np.mean(distances)
            self._means = means
            return means
        else:
            return self._means

    @property
    def stdevs(self):
        if self._stdevs is None:
            stdevs = {}
            for drunk, distances in self.distances.items():
                stdevs[drunk] = np.std(distances)
            self._stdevs = stdevs
            return stdevs
        else:
            return self._stdevs

    def show_plots(self):
        plt.show()


class WalkAnalysis(Analysis):

    linewidth = 0.4

    def __init__(self, walk_positions):
        super().__init__(walk_positions)

    def plot_paths(self):
        plt.figure(1)
        for drunk, positions in self.positions.items():
            x, y = zip(*positions)
            name = 'Drunk {}'.format(drunk.id)
            label_str = '{}\nMean: {}\nStdev: {}'.format(
                name,
                round(self.means[drunk], 2),
                round(self.stdevs[drunk], 2)
            )
            plt.plot(x, y, label=label_str, linewidth=self.linewidth)
        plt.legend()

    def plot_distances(self):
        plt.figure(2)
        for drunk, distances in self.distances.items():
            x = list(range(len(distances)))
            y = distances
            name = 'Drunk {}'.format(drunk.id)
            label_str = '{}\nMean: {}\nStdev: {}'.format(
                name,
                round(self.means[drunk], 2),
                round(self.stdevs[drunk], 2)
            )
            plt.plot(x, y, label=label_str, linewidth=self.linewidth)
        plt.legend()


class SimAnalysis(Analysis):

    def __init__(self, sim_positions):
        super().__init__(sim_positions)

    def plot_positions(self):
        plt.figure(3)
        for drunk, positions in self.positions.items():
            x, y = zip(*positions)
            name = 'Drunk {}'.format(drunk.id)
            label_str = '{}\nMean: {}\nStdev: {}'.format(
                name,
                round(self.means[drunk], 2),
                round(self.stdevs[drunk], 2)
            )
            alpha = 0.5 / len(self.positions)
            plt.scatter(x, y, label=label_str, alpha=alpha)
        plt.legend()
