from numpy import *
import matplotlib.pyplot as plt

theta = linspace(0,2*pi,100)

R = [i*sin(5*theta) for i in range(10)]
for r in R:
    plt.polar(theta,r)
plt.show()
