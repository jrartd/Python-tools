import matplotlib.pyplot as plt

edades = [12,14,15,16,17,11,19,20,16,14,17,17,19,20]
colores =["red","blue","green","yellow","black"]
his = plt.hist(edades,bins=5, color="red", orientation="horizontal")
plt.title("Grafico de edades y publicos objetivos") 	#el titulo
plt.ylabel("rango de edades")
print(plt.show())
