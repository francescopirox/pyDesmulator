# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from simulator import Simulator
from station import Station

if __name__ == '__main__':

    s=Simulator(1050)
    st1 = Station(None, None,s)
    s.start_simulation()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
