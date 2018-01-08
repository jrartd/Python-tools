#de esta forma se imprime un dicionario completo
hola = {"nombre":"jorge","apellido":"robalino","edad":25}

#los argumentos x, y recorren la lista y iteran toda 

for x,y in hola.items():
	print ("mi ",x ,"es",y )




"""
Con Numpy
"""
import numpy as np
height = np.array([10,23,12,24,36,57,67])
weight = np.array([23,45,23,24,25,89,89])

mix = np.array([height,weight])
for x in np.nditer(mix): # la funcion nditer
	print(x) 