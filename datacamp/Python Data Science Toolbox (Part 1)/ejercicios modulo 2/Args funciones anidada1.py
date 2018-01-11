def tweets(*args):
	for x in args: #cada elemento dentro de la lista es x #args se llma sin *
		if x <10:
			print(x)
		else:
			print("nada")

tweets(2,6,20,8,9,3,15)