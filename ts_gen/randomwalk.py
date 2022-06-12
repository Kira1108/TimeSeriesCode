import numpy as np
import random
from dataclasses import dataclass


@dataclass
class SimpleRandomWalk:
    """Genearte RandomWalk timeseries of n datapoints
    This randomwalk starts with `initial_value`
    shifts on each timestep controlled by `low` and `high`
    """
    n:int = 100
    initial_value:int = None
    low:float = -1
    high:float = 1

    @property
    def start(self):
        return self.initial_value or random.randint(1,10)

    def generate(self):
        series = []
        current = self.start

        for _ in range(self.n):
            current += self.low + (self.high - self.low) * random.random()
            series.append(current)

        return np.arange(self.n), np.array(series)


@dataclass
class GaussianRandomWalk:
    """Genearte Gaussian timeseries of n datapoints"""
    n:int = 100
    initial_value:int = None
    mu:float = 0
    sigma:float = 1

    @property
    def start(self):
        return self.initial_value or random.randint(1,10)


    def generate(self):
        series = []
        current = self.start

        for _ in range(self.n):
            current += np.random.normal(self.mu, self.sigma)
            series.append(current)

        return np.arange(self.n), np.array(series)