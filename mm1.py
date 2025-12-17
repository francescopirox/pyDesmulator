from stations.clientgenerator import ClientGenerator
from distributions.exponentialDistribution import *
from observers.observer import Observer
from simulators.simulator import Simulator
from stations.singleserverstation import SingleServerStation

# Coda MM1

print("simulatore coda m/m/1")
lamb = input("inserisci lambda:     ")
mu = input("inserisci mu:       ")
d_lamb = ExponentialDistribution(float(lamb))
d_mu = ExponentialDistribution(float(mu))

time = int(input("inserisci il tempo di simulazione: "))
total_time = time
s = Simulator(time)
s.trace = True
o = Observer()
st = SingleServerStation(o, s, d_mu)
gen = ClientGenerator(st, None, s, d_lamb)

print("**SIMULAZIONE IN CORSO** \n\n")
s.start_simulation()
o.output(total_time)
print("\n\n")
st.print_state()
time = int(input("inserisci il nuovo tempo di simulazione per continuare, -1 per completare: "))
while time > 0:
    total_time += time
    s.resume_simulation(time)
    print("**SIMULAZIONE IN CORSO** \n \n")
    o.output(total_time)
    print("\n")
    st.print_state()
    time = int(input("inserisci il nuovo tempo di simulazione per continuare, -1 per completare: "))
