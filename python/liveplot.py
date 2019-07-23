import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

x = [0]*10
y = [0]*10

def animate(i):
    x.append(random.randint(0,10))
    y.append(y[-1]+1)
    ax1.clear()
    ax1.plot(x,y)

ani = animation.FuncAnimation(fig, animate,interval=1000)
plt.show()
