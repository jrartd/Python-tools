import numpy as np
import matplotlib.pyplot as plt 

u = np.linspace(-1,9,50)
v = np.linspace(-1,8,60)

u,v = np.meshgrid(u,v)

z = u**2 + v**4/2

plt.pcolor(z)
plt.colorbar()

plt.show()