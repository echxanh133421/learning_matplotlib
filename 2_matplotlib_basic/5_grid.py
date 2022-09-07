import math

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,2*math.pi,0.05)
y=np.sin(x)

plt.plot(x,y)
plt.xlabel('trục x')
plt.ylabel('trục y')
plt.title('đồ thị y=sin(x)')
plt.grid(linestyle='-.',c='g',linewidth='0.5')
plt.show()