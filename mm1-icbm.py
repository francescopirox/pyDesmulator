# Coda MM1 Con IC
from observers.BMICobserver import BMICObserver
from stations.clientgenerator import ClientGenerator
from distributions.exponentialDistribution import ExponentialDistribution
from simulators.simulator import Simulator
from stations.singleserverstation import SingleServerStation

print("simulatore coda m/m/1")
lamb = input("inserisci     lambda:      ")
mu = input("inserisci      mu:          ")
d_lamb = ExponentialDistribution(float(lamb))
d_mu = ExponentialDistribution(float(mu))
classi=25
durata=250000000
transitorio=100000


s = Simulator(durata)
s.trace = False

o = BMICObserver(transitorio ,durata, classi)
st = SingleServerStation(o, s, d_mu)
gen = ClientGenerator(st, None, s, d_lamb)

print("**SIMULAZIONE IN CORSO** \n\n")

s.start_simulation()

o.output(durata)