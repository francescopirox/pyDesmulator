# Coda MM1 Con IC
from BMICobserver import BMICObserver
from clientgenerator import ClientGenerator
from exponentialDistribution import ExponentialDistribution
from icobserver import Icobserver
from simulator import Simulator
from singleserverstation import SingleServerStation

print("simulatore coda m/m/1")
lamb = input("inserisci     lambda:      ")
mu = input("inserisci      mu:          ")
d_lamb = ExponentialDistribution(float(lamb))
d_mu = ExponentialDistribution(float(mu))
classi=25
durata=100000000
transitorio=100000


s = Simulator(durata)
s.trace = False

o = BMICObserver(transitorio ,durata, classi)
st = SingleServerStation(o, s, d_mu)
gen = ClientGenerator(st, None, s, d_lamb)

print("**SIMULAZIONE IN CORSO** \n\n")

s.start_simulation()

o.output(durata)