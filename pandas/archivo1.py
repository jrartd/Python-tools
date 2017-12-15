import pandas as pd #organiza los datos
import matplotlib.pyplot as plt #permite generar graficas
import numpy as np #ayuda con los caculos

#organiza los datos del documneto csv 
data = pd.read_csv("VC.txt",header=0,delim_whitespace=True) #header significa que liena sera el titular
x= data.ix[:,0]
y= data.ix[:,1]
z= data.ix[:,2]

print (data)
print (x)
print (y)

#nos genera la grafica con los puntos de dispersion
plt.plot(x,y,"ro")
plt.ylabel("carreras")
plt.xlabel("turnos al bat")
plt.show()

#scipy
coefciente = np.polyfit(x,y,1)
polinomio = np.polyld(coefciente)
print (polinomio)