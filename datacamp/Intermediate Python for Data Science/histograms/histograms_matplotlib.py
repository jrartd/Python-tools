import matplotlib.pyplot as plt 
data = [14,33,44,25,36,47,51,31,22,32,53,72,71,2,81,92,21,32,41,52,21,123]
plt.title("Grafico de edades") 	#el titulo
plt.ylabel("Edades en edad")	#etiquetas del eje x
plt.xlabel("grupos de edad")	#etiquetas de eje y
plt.hist(data,bins=10,color="red",orientation="horizontal",) # plt.hist(variable con datos,bins= numero de columnas)
plt.yticks([10,20,40,60,80,100,120],["24años","35 años","45 años","55años","65años","75años","85años"]) 	#cambia los indices para mejorar la visualización en y
plt.show()