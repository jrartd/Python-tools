import pandas as pd 
datageneral = pd.read_csv("./gapminder.csv", index_col=0)
datosx = datageneral[["life_exp"]]
datosxround =round(datosx,0)
datosy = datageneral[["gdp_cap"]]
paises = datageneral[["cont"]]
print (datosxround)
#print (datosy)

import numpy as np
datosxsize = np.array(datosx)
datosxsize2 = datosxsize *6

import matplotlib.pyplot as plt 
color = ["red","blue","green","yellow","black"]
grafi = plt.scatter(datosxround,paises, alpha=0.7, c=color)
plt.xlabel("ciclo de vida")
plt.ylabel("tasa de dispersion")

plt.xticks([0,10,20,30,40,50,60,70,80],[40,50,60,70,80])
plt.show()
