import numpy as np
import matplotlib.pyplot as plt 


A = np.array([[1, 0, -1], [2, 0, 1], [1, 1, 1]])

x,y = np.meshgrid(A[0],A[1])

z =A[2] + A[1]

plt.set_cmap("nipy_spectral") 
plt.pcolor()
plt.colorbar()
plt.show()
