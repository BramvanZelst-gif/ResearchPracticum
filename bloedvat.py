import matplotlib.pyplot as plt
import math as mt
import numpy as np
from matplotlib.animation import FuncAnimation 

# Constante waardes 
C = 7 * 10**-9
rho = 1060
A = np.pi * 0.0004**2
N = 500
dx = 0.01/N

s = 0.001
c = np.sqrt(A/rho/C)
dt = s/c/N
# dt = 0.001/ 0.26  /N

# initiële condities
P_start = []
for i in range(0, N):
    P_start.append(80)

# for i in np.arange(0, 0.01, 0.01/N):
#     p = 40 * np.exp(-(i**2 / 0.002**2)) + 80
#     P_start.append(p)

Q_start = []
for i in range(0, N):
    Q_start.append(0)

def bepaal_dqdx(Q_lijst):
    dqdx_lijst = []
    for i, flow in enumerate(Q_lijst): 
    
        if i == 0:
            dqdx = (Q_lijst[i+1] - Q_lijst[i]) / dx

        elif i == len(Q_lijst)-1:
            dqdx = (Q_lijst[i] - Q_lijst[i-1]) / dx

        else:
            dqdx = (Q_lijst[i+1] - Q_lijst[i-1]) / 2 / dx

        dqdx_lijst.append(dqdx)

    return dqdx_lijst


def bepaal_P(Q_lijst, P_lijst, n):
    dqdx_lijst = bepaal_dqdx(Q_lijst)
    P_lijst2 = []

    for i in range (len(dqdx_lijst)):
        if i == 1:
            P = 40 * np.sin(2 * np.pi * n / 0.006) + 80
            P_lijst2.append(P)
            
        else:
            dpdt = dqdx_lijst[i]/-C
            P = P_lijst[i] + dpdt * dt
            P_lijst2.append(P)


    
    return P_lijst2


def bepaal_dpdx(Q_lijst, P_lijst):
    P_lijst2 = bepaal_P(Q_lijst, P_lijst, n)
    dpdx_lijst = []
    for i, flow in enumerate(P_lijst2):  

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
plaats = []
for i in range(0, N):
    plaats.append(i * dx)

n = 0
for t in np.arange(0, 10*N):
    p = bepaal_P(Q_start, P_start, n)
    q = bepaal_Q(Q_start, P_start)
    n = n + 0.001

    if t%100 == 0:
        plt.plot(plaats, P_start)
        plt.draw()
        plt.pause(0.01)
        plt.clf()

    P_start = p
    Q_start = q
    
    P.append(p)


plt.plot(plaats, P_start)
plt.show()

print(len(P_start))
print(len(plaats))