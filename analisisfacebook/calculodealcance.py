#importacion
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

#seleccion de data
mainData = pd.read_csv("diciembre.csv",index_col=0)

#seleccion de fecha
datecolum = mainData.iloc[1:,5]
npdatecolum = np.array(datecolum)


def CalculoDeAlcance():
	#alcance total
	alcancecolum = mainData.iloc[1:,7]
	alcancecolum.astype(int)

	print (type(alcancecolum))
	#convertir columnas en numpy
	npalcancecolum = np.array(alcancecolum)



	#graficas
	plt.ylabel("Alcance ")
	plt.xlabel("Dias del mes ")
	plt.title("Cuadro total de Alcance del mes ")
	plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,2,25,26,27,28,28,30,31],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,2,25,26,27,28,28,30,31])
	plt.scatter(npdatecolum,npalcancecolum)
	plt.plot(npdatecolum,npalcancecolum)

	#mostrar
	plt.grid()
	plt.show()

calculoDeAlcance()