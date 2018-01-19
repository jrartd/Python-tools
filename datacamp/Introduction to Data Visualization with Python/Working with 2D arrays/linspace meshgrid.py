import matplotlib.pyplot as plt 

#meshgrid
import numpy as np 
u = np.linspace(-2,2,10)
v = np.linspace(-1,1,10)

x,y = np.meshgrid(u,v)

Z = x**2/5 + y**2/30
print("Z:",Z)
plt.set_cmap("nipy_spectral")
plt.pcolor(Z)
plt.show()