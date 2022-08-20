import random

from distribution import Distribution

# Distribuzione Esponenziale

class ExponentialDistribution(Distribution):
    l_value=0
    r= random.Random()

    def __init__(self, l_value) -> None:
        super().__init__()
        self.l_value=l_value
        self.r.seed()


    def next_sample(self):
        return int(self.r.expovariate(self.l_value)*1000)

    def change_seed(self):
        self.r.seed()



