import observer
from clientgenerator import ClientGenerator
from exponentialDistribution import ExponentialDistribution
from BMICobserver import BMICObserver
from simulator import Simulator
from singleserverstation import SingleServerStation

# Coda MM1 Con IC

print("simulatore coda m/m/1")
lamb = input("inserisci lambda:     ")
mu = input("inserisci mu:         ")
d_lamb = ExponentialDistribution(float(lamb))
d_mu = ExponentialDistribution(float(mu))

time = int(input("inserisci il tempo di simulazione: "))
total_time = time
s = Simulator(time)
s.trace = False
o = BMICObserver(2000,2000,30)
st = SingleServerStation(o, s, d_mu)
gen = ClientGenerator(st, None, s, d_lamb)

print("**SIMULAZIONE IN CORSO** \n\n")
s.start_simulation()
print("\n")
st.print_state()
print(o.state())
time = int(input("inserisci il nuovo tempo di simulazione per continuare, -1 per completare: "))

while time > 0:
    total_time += time
    s.resume_simulation(time)
    print("**SIMULAZIONE IN CORSO** \n \n")
    o.ouput(total_time)
    print("\n")
    st.print_state()
    time = int(input("inserisci il nuovo tempo di simulazione per continuare, -1 per completare: "))

ic=o.get_waiting_time_ic(total_time)
print(ic.mean_value)
print(ic.quantile)