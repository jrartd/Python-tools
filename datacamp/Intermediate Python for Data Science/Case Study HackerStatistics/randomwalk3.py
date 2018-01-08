import numpy as np
import matplotlib.pyplot as plt 
np.random.seed(1234)

lista = [0]

for x in range (5000):
	crecimiento= lista[-1]
	random= np.random.randint(0,10)

	if random <=2 :
		crecimiento = max(0 , crecimiento - 1) #primer atributo es el minimo ,
	elif random <=9 :
		crecimiento = crecimiento + 1
	else:
		crecimiento + np.random.randint(0,10)

	lista.append(crecimiento)

#print(lista)

#plt.plot(lista)
plt.grid()
plt.hist(lista,bins=100)
plt.show()

hola = np.array([1,2,3],[4,5,6])
holanp = np.transpose(hola)
print(hola)
print(holanp)
