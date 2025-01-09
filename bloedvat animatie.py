import matplotlib.pyplot as plt
import math as mt
import numpy as np
import matplotlib.animation as ani
# from matplotlib.animation import FuncAnimation 

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

# Constante waardes 
C = 7 * 10**-9
rho = 1060
A = np.pi * 0.0004**2

N = 18
x_max = 0.01
x_min = 0
dx = (x_max - x_min) / N
x = []
for i in range(0,N):
    x_min = x_min + dx
    x.append(x_min)

# in 1 cm had het 0.38s nodig, c = 0,26 m/s, t = s/v
t_max = 0.038
t_min = 0
dt = (t_max - t_min) / N
t = []
for i in range(0,N):
    t_min = t_min + dt
    t.append(t_min)
c = 0.26 # = np.sqrt(A/rho/C)

# initiele condities
P_start = [120, 100, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
Q_start = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# animatie waardes
fps = 10   # frames per second in animation
total_time = 18  # in seconds, total time of animation
time_ratio = 100 # in seconds, how many seconds in reality for every second on animation

# extra calculations
interval = 1/fps # in seconds
total_frames = 18
total_time = 18 / 10

fig = plt.figure()
ax = plt.gca()

P = []
for i in range(0,18):
    p = bepaal_P(Q_start, P_start)
    q = bepaal_Q(Q_start, P_start)
    P_start = p
    Q_start = q
    
    P.append(p)

def animation(i): 
    global x, P

    ax.clear()
    plt.plot(x, P[i])

# animation = FuncAnimation(fig, animation, interval = 100)
anim = ani.FuncAnimation(fig, animation, frames = range(total_frames), interval = interval)
anim.save("test.mp4", fps = fps)
plt.show()
