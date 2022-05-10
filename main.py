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
    o.ouput()
    print(str(o.working_time))
    print("utilizzazione servente:"+ str(o.get_utilizzazione(1000000)))
    print("througput:"+ str(o.get_throughput(1000000)))
    print("mean number client in line or in service:" + str(o.get_mean_client_queue_or_service(1000000)))
    print("W:" + str(o.get_waiting_time(1000000)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
