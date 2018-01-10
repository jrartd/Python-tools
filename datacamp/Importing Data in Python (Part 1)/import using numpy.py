import numpy as np
#loadtxt
maindata = np.loadtxt("seaslug.txt",delimiter='\t',skiprows=1,dtype=str) #para importar se usa numpy
primera = maindata[6:5]
#print(maindata)


#PARA USAR genfromtxt se debe colocar todos estos atribtos
data = "titanic_sub.csv"
npdata = np.genfromtxt(data,delimiter=",",names=True,dtype=None,)
#print (npdata["Survived	"])

#recfromcsv ya tiene por defecto todos los atributos es el que mas voy a usar
datatic = "titanic_sub.csv"
titac = np.recfromcsv(datatic)
print (titac)