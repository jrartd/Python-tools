#importacion
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

#seleccion de data
mainData = pd.read_csv("publidiciembre.csv",index_col=0)

#seleccion de fecha
datecolum = mainData.iloc[0:,6]
npdatecolum = np.array(datecolum)
scala = np.array([0,100,900])
npshare = np.array(mainData.iloc[0:,8])
nplike =np.array(mainData.iloc[0:,9])
npcomment=np.array(mainData.iloc[0:,10])

plt.title("Grafica comparativa entre likes, shares y comentarios")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,2,25,26,27,28,28,30,31],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,2,25,26,27,28,28,30,31])
plt.yticks([0,300,500,700,1000,2000,3000,4000,5000])

plt.scatter(npdatecolum,nplike)
plt.plot(npdatecolum,npshare, color="red",label="Shares ")
plt.plot(npdatecolum,npcomment, color="#F89406",label="Comentarios")
plt.plot(npdatecolum,nplike, color="blue", label="Likes")

#el atributo legend crea los cuadros de dalogos
legend = plt.legend(loc='upper right')
legend.get_frame().set_facecolor('white')

plt.grid(True)
plt.show()
