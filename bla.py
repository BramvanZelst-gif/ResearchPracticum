P00 = 0         # bovendruk - 120, onderdruk - 80
P01 = 1
P02 = 1
P03 = 0

Q00 = 0
Q01 = 0
Q02 = 0
Q03 = 0

P10 = 0
P11 = 1
P12 = 1
P13 = 0

# bovendruk - 120
# onderdruk - 80
# Your aorta, your largest artery, is about 10 millimeters (mm) to 25 mm (.4 inch to .9 inch) in diameter. Other arteries can be 3 mm to 5 mm 
# (.11 inches to .19 inches) in diameter, while the smallest arteries, arterioles, can be .30 mm to .01 mm in diameter. 
# -- denk die van 3 tot 5 mm voor ons en daarmee oppervlakte bepalen.
# c = golfsnelheid in m/s, 

# eerst dQ/dx om dP/dt te berekenen.
# grote C nodig daarvoor
# Nu kunnen we P berekenen voor volgende tijdstip
# Nu kunnen we dP/dx gebruiken voor dQ/dt
# dichtheid p en A nodig daarvoor, A constant?
# Nu kunnen we Q berekenen voor volgende tijdstip
# opnieuw 


P_max = 120
P_min = 80

N = 10
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


P_start = []
