import random

from distribution import Distribution


class ExponentialDistribution(Distribution):
    l_value=0

    def __init__(self, l_value) -> None:
        super().__init__()
        self.l_value=l_value

    def next_sample(self):
        return int(random.expovariate(self.l_value)*1000)





