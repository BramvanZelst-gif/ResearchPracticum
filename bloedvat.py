import matplotlib.pyplot as plt
import math as mt
import numpy as np


# Constante waardes 
C = 1
rho = 1
A = 1
dx = 1
dt = 1


# initiele condities
P_start = [1, 1, 2, 1, 1]
Q_start = [0, 0, 0, 0, 0]

def bepaal_dqdx(Q_lijst):
    dqdx_lijst = []
    for i, flow in enumerate(Q_lijst):  # Gebruik enumerate om de index te krijgen
    
        if i == 0:
            dqdx = Q_lijst[i+1] - Q_lijst[i] / dx

        elif i == len(Q_lijst)-1:
            dqdx = Q_lijst[i] - Q_lijst[i-1] / dx

        else:
            dqdx = (Q_lijst[i+1] - Q_lijst[i-1]) / 2 / dx

        dqdx_lijst.append(dqdx)

    return dqdx_lijst


def bepaal_P(Q_lijst, P_lijst):
    dqdx_lijst = bepaal_dqdx(Q_lijst)
    P_lijst2 = []

    for i in range (len(dqdx_lijst)):
        dpdt = dqdx_lijst[i]/-C
        P = P_lijst[i] + dpdt * dt
        P_lijst2.append(P)
    
    return P_lijst2


def bepaal_dpdx(Q_lijst, P_lijst):
    P_lijst2 = bepaal_P(Q_lijst, P_lijst)
    dpdx_lijst = []
    for i, flow in enumerate(P_lijst2):  # Gebruik enumerate om de index te krijgen
    
        if i == 0:
            dpdx = P_lijst2[i+1] - P_lijst2[i] / dx

        elif i == len(Q_lijst)-1:
            dpdx = P_lijst2[i] - P_lijst2[i-1] / dx

        else:
            dpdx = (P_lijst2[i+1] - P_lijst2[i-1]) / 2 / dx

        dpdx_lijst.append(dpdx)

    return dpdx_lijst




def bepaal_Q(Q_lijst, P_lijst):
    dpdx_lijst = bepaal_dpdx(Q_lijst, P_lijst)
    Q_lijst2 = []

    for i in range (len(dpdx_lijst)):
        dqdt = dpdx_lijst[i] *A / -rho
        print(dqdt)
        Q = Q_lijst[i] + dqdt * dt
        Q_lijst2.append(Q)
    
    return Q_lijst2


P = [P_start]
plaats = [0,1,2,3,4]
for t in range(0,5):
    p = bepaal_P(Q_start, P_start)
    q = bepaal_Q(Q_start, P_start)
    plt.plot(plaats, P_start)
    plt.show()
    P_start = p
    Q_start = q
    
    P.append(p)

plt.plot(plaats, P_start)
plt.show()