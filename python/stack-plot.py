import matplotlib.pyplot as plt
import random

sleeping = [7, 8, 6, 11, 7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

# Just for legends
plt.plot([],[], color='m', label='sleeping', linewidth=5)
plt.plot([],[], color='c', label='eating', linewidth=5)
plt.plot([],[], color='r', label='working', linewidth=5)
plt.plot([],[], color='k', label='playing', linewidth=5)
plt.legend()

plt.stackplot(sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
plt.show()

