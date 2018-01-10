#defnir una funcion
def funcion():
	pass

#pasar dos parametros
def funcion1(x,n):
	print (x + n)
funcion1(5,7)


#TUPLAS


#funcio dentro de una funcion
def funcion2(f):
	def funcion21(x,v):
		hi = 6 + 8 + x + v + f
		print (hi)
	funcion21(10,14)
funcion2(6)