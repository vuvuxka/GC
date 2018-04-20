import matplotlib.pyplot as plt
#from createpoints import *

fig = plt.figure()
ax = plt.subplot(111)
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
    
start = CreatePoints(fig, ax)
plt.show()