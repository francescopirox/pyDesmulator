# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from clientgenerator import ClientGenerator
from exponentialDistribution import ExponentialDistribution
from simulator import Simulator
from singleserverstation import SingleServerStation

if __name__ == '__main__':
    s = Simulator(10000)
    d = ExponentialDistribution(10)
    st1 = SingleServerStation(None, s, d)
    gen = ClientGenerator(st1, None, s, d)

    s.start_simulation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
