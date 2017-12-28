#Metodos son funciones que le pertenecen a objetos
#En python todo es un objecto
fam = [1.4523,1.56,1.90,1.67,2.00,1.23]
print(fam.index(1.90)) #aqui se expresa la funcion index() como un metodo dentro de la lista
    #Append() --- suma objetos a una lista
fam.append("hola")
print (fam)


    # Round() --- Cuenta el numero de veces que un item se encuentra en la variable
room = "poolhouse"
print (room.count("o"))