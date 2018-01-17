import matplotlib.pyplot as plt 
#axes(x,y,width,height)
import pandas as pd
import numpy as np

data = pd.read_csv("brics.csv",index_col=0)

columnapd  = pd.DataFrame(data)
columnaa = columnapd[["population"]]
MSFTaa =  columnapd[["area"]]
plt.axes([0.05,0.05,0.15,0.9]) #se debe generar un axes por cada cuadro que se genere
plt.plot(MSFTaa)
plt.axes([0.2,0.05,0.15,0.9]) #se debe generar un axes por cada cuadro que se genere
plt.plot(MSFTaa)


plt.show()
print(columnaa)