import pandas as pd
texto1 = pd.read_csv("../pandas/gapminder.csv",index_col=0)

paises = texto1["country"] # selecciono la columna
seleccion = (paises == "Argentina") # selecciono el campo que se repite
print (texto1[seleccion]) # imprimo solo los campos selecionados




# FORMA 2

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr =cars["drives_right"]

# Use dr to subset cars: sel
sel =(cars[dr])

# Print sel
print (sel)


