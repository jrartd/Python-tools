#funciones anidadas
def edades(key):
	edad = key
	def mul(value):
		hola = value + edad
		print (hola)

	mul(10)
edades(15)


"""
con global puedo usar las variables globales sin modificar la original
co nonlocal modifico las variables globales
"""








