# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from clientgenerator import ClientGenerator
from exponentialDistribution import ExponentialDistribution
from observer import Observer
from simulator import Simulator
from singleserverstation import SingleServerStation

if __name__ == '__main__':
    s = Simulator(1000000)
    o = Observer()
    lamb = ExponentialDistribution(1.5)
    d1 = ExponentialDistribution(2)
    st1 = SingleServerStation(o, s, d1)
    gen = ClientGenerator(st1, None, s, lamb)

    s.start_simulation()
    o.output(1000000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
