import pandas as pd
import matplotlib.pyplot as plt
maindata = pd.read_csv("../datasets/pokemon.csv")


"""
Melt convierte columnas en filas
"""
#melt = pd.melt(frame=, id_vars="", value_vars="",id_name="", value_name="")
melt = pd.melt(frame=maindata, id_vars=["Name","Total","HP","Attack","Defense","Sp. Atk"], value_vars=["Type 1","Type 2"], var_name="Tipo", value_name="Clase")
print (melt)
