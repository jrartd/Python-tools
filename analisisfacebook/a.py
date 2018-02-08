import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


maindata = pd.read_excel("./enero.xls", sheetname="ciudad")
fecha = maindata["Fecha"]
gye = maindata["Guayaquil, Provincia del Guayas, Ecuador"]
plt.plot(fecha, gye,label="Guayaquil" )
plt.plot(fecha, maindata["Ibarra, Provincia de Imbabura, Ecuador"],label="Ibarra" )
plt.plot(fecha, maindata["Manta, Provincia de Manabí, Ecuador"],label="Manta" )
plt.plot(fecha, maindata["Quito, Provincia de Pichincha, Ecuador"],label="Quito" )
plt.plot(fecha, maindata["Riobamba, Provincia de Chimborazo, Ecuador"], label="Riobamba")
plt.plot(fecha, maindata["Santo Domingo (Ecuador), Provincia de Santo Domingo de los Tsáchilas, Ecuador"], label="Santo Domingo")
plt.plot(fecha, maindata["Ambato, Provincia de Tungurahua, Ecuador"],label="Ambato" )
plt.plot(fecha, maindata["Cuenca, Provincia de Azuay, Ecuador"],label="Cuenca" )
plt.legend(bbox_to_anchor=(1, 1))
plt.grid()
plt.show()