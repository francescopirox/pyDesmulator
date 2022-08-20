
from clientgenerator import ClientGenerator
from exponentialDistribution import ExponentialDistribution
from icobserver import Icobserver
from simulator import Simulator
from singleserverstation import SingleServerStation

# Coda MM1 Con IC

print("simulatore coda m/m/1")
lamb = input("inserisci     lambda:      ")
mu = input("inserisci      mu:          ")
d_lamb = ExponentialDistribution(float(lamb))
d_mu = ExponentialDistribution(float(mu))
classi=25
durata=1000000


s = Simulator(durata)
s.trace = False
o = Icobserver(classi, durata, transitorio)
st = SingleServerStation(o, s, d_mu)
gen = ClientGenerator(st, None, s, d_lamb)

print("**SIMULAZIONE IN CORSO** \n\n")
for  i in range(0,classi):
    s.start_simulation()
    o.cambia_osservatore()
    s.reset()

o.output(durata)