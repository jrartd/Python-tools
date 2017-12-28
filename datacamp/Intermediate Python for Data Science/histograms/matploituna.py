import matplotlib.pyplot as plt
year = [1992,1993,1994,1995]
pop = [12345,34234,38456,42345]

import numpy as np 
sizelist = np.array(pop)
size = sizelist/16
colors = ['#624ea7', 'g', 'yellow', 'k', 'maroon']
plt.plot(year,pop,) #plt.plot() coteja los indices x y y y los grafica con una linea
plt.scatter(year,pop,s=size,c =colors) #plt.scatter() muestra los puntos  s es el atribto de escala de los puntos
#para crear colores debemos crear una lista con os colores y asgnarselo al atributo "C"
plt.show()