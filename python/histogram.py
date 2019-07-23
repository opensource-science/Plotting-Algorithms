import matplotlib.pyplot as plt
import random

x = [random.randint(1, 130) for i in range(50)]
y = [0,10,20,30,40,50,60,70,80,90,100,120,130]

plt.hist(x,y, histtype='bar', rwidth=0.8)
plt.show()
