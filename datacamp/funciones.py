#funciones
    # Max()-- enuentra el numero mayor dentro de una lista
fam = [1.4523,1.56,1.90,1.67,2.00,1.23]
print(max(fam))

print(min(fam))

    # abs() -- Retorna el numero absolto desde el cero
numero = -5.2
print (abs(numero))

    # round() -- La funcion tiene dos parametros (valor a redondear, y cantidad de decimales)
print (round(3.53))
print (sorted(fam))

    #len() -- me permite saber el tamaño de una cadena
print(len(fam))

    #sorted
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second
full_sorted= sorted(full, reverse=True)
print (full_sorted)