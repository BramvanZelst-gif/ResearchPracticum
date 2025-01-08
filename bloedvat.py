import matplotlib.pyplot as plt
import math as mt
import numpy as np
from matplotlib.animation import FuncAnimation 

# Constante waardes 
C = 7 * 10**-9
rho = 1060
A = np.pi * 0.0004**2
dx = 0.001
dt = 0.00384
print(np.sqrt(A/rho/C))

# initiele condities
P_start = [80, 80, 80, 100, 120, 100, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
Q_start = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def bepaal_dqdx(Q_lijst):
    dqdx_lijst = []
    for i, flow in enumerate(Q_lijst):  # Gebruik enumerate om de index te krijgen
    
        if i == 0:
            dqdx = (Q_lijst[i+1] - Q_lijst[i]) / dx

        elif i == len(Q_lijst)-1:
            dqdx = (Q_lijst[i] - Q_lijst[i-1]) / dx

        else:
            dqdx = (Q_lijst[i+1] - Q_lijst[i-1]) / 2 / dx

        dqdx_lijst.append(dqdx)

    return dqdx_lijst


def bepaal_P(Q_lijst, P_lijst):
    dqdx_lijst = bepaal_dqdx(Q_lijst)
    P_lijst2 = []
    dpdt_lijst = []

    for i in range (len(dqdx_lijst)):
        dpdt = dqdx_lijst[i]/-C
        P = P_lijst[i] + dpdt * dt
        P_lijst2.append(P)
        dpdt_lijst.append(dpdt)
    print(dpdt_lijst)

    
    return P_lijst2


def bepaal_dpdx(Q_lijst, P_lijst):
    P_lijst2 = bepaal_P(Q_lijst, P_lijst)
    dpdx_lijst = []
    for i, flow in enumerate(P_lijst2):  # Gebruik enumerate om de index te krijgen
    
        if i == 0:
            dpdx = (P_lijst2[i+1] - P_lijst2[i]) / dx

        elif i == len(Q_lijst)-1:
            dpdx = (P_lijst2[i] - P_lijst2[i-1]) / dx

        else:
            dpdx = (P_lijst2[i+1] - P_lijst2[i-1]) / 2 / dx

        dpdx_lijst.append(dpdx)

    return dpdx_lijst




def bepaal_Q(Q_lijst, P_lijst):
    dpdx_lijst = bepaal_dpdx(Q_lijst, P_lijst)
    Q_lijst2 = []

    for i in range (len(dpdx_lijst)):
        dqdt = dpdx_lijst[i] *A / -rho
        
        Q = Q_lijst[i] + dqdt * dt
        Q_lijst2.append(Q)
    
    return Q_lijst2


P = [P_start]
plaats = [0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.010, 0.011, 0.012, 0.013, 0.014, 0.015, 0.016, 0.017]
for t in range(0,18):
    p = bepaal_P(Q_start, P_start)
    q = bepaal_Q(Q_start, P_start)
    
    plt.plot(plaats, P_start)
    plt.show()
    P_start = p
    Q_start = q
    
    P.append(p)

plt.plot(plaats, P_start)
plt.show()