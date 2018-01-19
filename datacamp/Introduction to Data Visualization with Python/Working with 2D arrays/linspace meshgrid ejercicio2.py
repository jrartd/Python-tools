import numpy as np 
import matplotlib.pyplot as plt 

#los steps estan definidos por a cantidad de atributos en la lista
u = np.array([0,3,4,5,12,6])
v = np.array([4,6,7,8,9,0])

x,y= np.meshgrid(u,v)

z = x**24/5 + y**12/4
plt.set_cmap("nipy_spectral")
plt.pcolor(z)
plt.colorbar()
plt.show()