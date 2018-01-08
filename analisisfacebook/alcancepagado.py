#importacion
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

#seleccion de data
mainData = pd.read_csv("diciembre.csv",index_col=0)

#seleccion de fecha
datecolum = mainData.iloc[1:,5]
npdatecolum = np.array(datecolum)


def alcancepagado():
	alcancepagadocolum = mainData.iloc[1:,9]

	#convertir nparray
	npalcancepagadocolum = np.array(alcancepagadocolum)

	#graficos
	plt.ylabel("Alcance Pagado")
	plt.xlabel("Dias del mes ")
	plt.title("Cuadro total de Alcance Pagado del mes ")
	plt.scatter(npdatecolum,npalcancepagadocolum)
	plt.grid(True)
	plt.show()
alcancepagado()