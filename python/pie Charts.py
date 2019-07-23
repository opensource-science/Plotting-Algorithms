import matplotlib.pyplot as plt
import random


slices = [7,2,2,13]
activities = ['sleep', 'work', 'play', 'eat']


plt.pie(slices, labels=activities,colors=['c','m','g','r'], startangle=90, shadow=True, explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.show()

