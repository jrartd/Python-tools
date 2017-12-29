#------> columns
import pandas as pd 

brics = pd.read_csv("./brics.csv", index_col=0) #nos permite leer un csv , index_col=0 hace que el index sea la columna 0
print (brics)
print ("\n")

cars = pd.read_csv("./cars.csv", index_col=0)
print (cars)
"""
"""
print ("\n")
print ("\n")
print ("\n")
gap = pd.read_csv("./gapminder.csv", index_col=0)
print (gap) 
