# Abrir archivo
file = open("moby_dick.txt")

print(file.read()) #leer el archivo


print(file.closed) #verificar si esta cerrado

file.close() #cerrar el archivo

print(file.closed) #verificar si esta cerrado


#_____________________________________________________

# leer las res primeras lineas
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
