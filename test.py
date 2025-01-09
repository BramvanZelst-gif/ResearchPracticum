import matplotlib.pyplot as plt
import matplotlib.animation as ani

# import moviepy.editor as mp

x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

y = []

# t = []
# for i in range(0,21):

#     t.append(i)
# y.append(t)

for j in range(0,10):
    t = []
    for k in range(0,21):

        t.append(k)
    y.append(t)

frames=20
fig = plt.figure()
ax = plt.gca()

def scatter_ani(i):
    global x, y
    # print(y[1])

    plt.plot(x, y[i])
    print(i)

anim = ani.FuncAnimation(fig, scatter_ani, frames=frames, interval=50)

plt.show()