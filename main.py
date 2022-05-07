# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from clientgenerator import ClientGenerator
from distribution import Distribution
from simulator import Simulator
from station import Station

if __name__ == '__main__':

    s=Simulator(1050)
    d=Distribution()
    st2 = Station(None, None, s)
    st1 = Station(st2, None, s)
    st2.next_station=st1
    gen=ClientGenerator(st1, None, s, d)

    s.start_simulation()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
