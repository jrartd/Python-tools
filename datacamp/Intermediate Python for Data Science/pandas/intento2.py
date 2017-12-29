import pandas as pd 
datageneral = pd.read_csv("./gapminder.csv", index_col=0)
datosx = datageneral[["life_exp"]]
datosy = datageneral[["gdp_cap"]]
paises = datageneral[["country"]]
#print (datosx)
#print (datosy)

import numpy as np
datosxsize = np.array(datosx)
datosxsize2 = datosxsize *6

import matplotlib.pyplot as plt 
color = ["red","blue","green","yellow","black"]
grafi = plt.scatter(datosx,paises, s= datosxsize2,alpha=0.7, c=color)
plt.xlabel("ciclo de vida")
plt.ylabel("tasa de dispersion")

plt.xticks([10,20,30,40,50,60,70,80,90,100])
plt.yticks([10,20,30,40,50,60,70,80,90,100])
plt.show()