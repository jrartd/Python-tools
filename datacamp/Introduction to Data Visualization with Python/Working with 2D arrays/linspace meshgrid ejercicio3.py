import numpy as np 
import matplotlib.pyplot as plt 

listasnos = []
def ejex(anonp,value):
	
	while (anonp < value):
		listasnos.append(anonp)
		anonp = anonp + 1
ejex(1900,2000)


indicey = []
def ejey(indice, value):
	while (indice < value):
			indicey.append(indice)
			indice = indice + 1 
ejey(0,1000)


#numpy 
ejex = np.array(listasnos)
ejey = np.array(indicey)

x,y = np.meshgrid(ejex, ejey)
z = x**2 + y**4

plt.set_cmap("nipy_spectral")
plt.contour(z)
plt.colorbar()
plt.show()

