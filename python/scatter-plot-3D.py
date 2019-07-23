import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = range(30)
ys = [np.cos(x) for x in np.arange(0,6e,0.2)]
zs = [np.sin(x) for x in np.arange(0,6,0.2)]
ax.scatter(xs, ys,zs)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
