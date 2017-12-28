
"""
np_height = np.array([2,4,5,6,6,7,7,8,8,8])
np_weight = np.array([1,7,5,9,0,3,2,1,2,7])
"""
#todos los elementos deben ser iguales
import numpy as np
np_2d = np.array([[1,3,5,8,4,5,7,7,7,4],[2,5,7,8,6,12,4,4,6,7]])
print (np_2d)
#para que shape funcione debe estar sin parentesis y debe tener mi np.arry igual numero de columnas y filas
print (np_2d.shape)


np_2d = np.array([[1,3,5,8,4,5,7,7,7,4],[2,5,7,8,6,12,4,4,6,7]])
print (np_2d[0][2])
print (np_2d[0,2]) # al coma es igual a los dos []
print (np_2d[:,2:4]) # [:,2:4] = : escoge todas las columnas, 2:4 del elemento 2 al 4