import matplotlib.pyplot as plt
import random

X = [random.randint(0, 2) for i in range(10)]
Y = [random.randint(0, 2) for i in range(10)]
dy = [random.randint(0, 2) for i in range(10)]
dx = [random.randint(0, 2) for i in range(10)]
for i in range(len(X)):
    plt.arrow(X[i],Y[i],dx[i], dy[i])
plt.show()

