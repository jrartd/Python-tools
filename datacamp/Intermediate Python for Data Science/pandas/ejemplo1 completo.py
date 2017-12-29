# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Crear diccionario donde introduzco las listas dentro de 
my_dict = {"country":names,"drives_right":dr,"cars_per_cap":cpc}

# convertir el dicionario normal en data para pandas
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Lista para cambiar por los index
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# cambiar los index normales por estos que esta en la lista  
cars.index=(row_labels)

# Print cars again
print(cars)

#seleccionar columnas especificas
print(cars[["cars_per_cap"]])

#ver el tipo de una columna
print (type(cars["country"])) #como panda
print (type(cars[["country"]])) #como dataframe


#formas de seleccionar con loc selecciono el indice
print(cars.loc[["RU","IN"]])


#formas de seleccionar con iloc selecciono el numero
print(cars.iloc[[1,2,3]])