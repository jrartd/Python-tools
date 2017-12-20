# las listas van en []
lista = [1, 2.5, 'DevCode', [5,6] ,4]
#metodos de una lista

"""     Append
Podemos agregar cualquier tipo de elemento a una lista, 
pero tengan en cuenta lo que pasa cuando agregamos una lista dentro de otra,
esta lista se agrega como uno y solo un elemento."""

lista.append("datacamp")
print(lista)

"""		Extend
Extend también nos permite agregar elementos dentro de una lista,
pero a diferencia de append al momento de agregar una lista,
cada elemento de esta lista se agrega como un elemento más dentro de la otra lista.
"""
lista.extend([7,8,9])
print(lista)

"""
	Remove
	El método remove va a remover un elemento que se le pase como parámentro
	de la lista a donde se le esté aplicando.
"""
#SLICING

print(lista[2:])
h = [["a", "b", "c"],["d", "e", "f"],["g", "h", "i"]]
print (h[0][1])

h[0][1] ="Hola soy un cambio"
print (h[0][1])

# cambiando elementos 
h[0][1] ="Hola soy un cambio"
print (h[0][1])

del(h[0]) # eliminando un elemento de una lista
print (h[0:])


#sumar elementos a una ista 
lista1 = [2,5,"hola"]
lista2 = lista1 + [3,"chau"]

print (lista2)

#cambiar elementos dentro de una lista
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print (areas)

areas[-1] = [10.95]
print ( areas)