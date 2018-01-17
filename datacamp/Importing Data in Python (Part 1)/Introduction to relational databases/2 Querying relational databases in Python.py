from sqlalchemy import create_engine

import pandas as pd 

engine = create_engine("sqlite:///Chinook.sqlite")#crea la base de datos
con = engine.connect()			#conecta la base de datos
rs = con.execute("SELECT * FROM Orders") #seleccion dentro de la base de datos
df = df.DataFrame(rs.fetchall()) #ESCOGE Y GUARDO TODA LA BASE DE DATOS
dfm = df.DataFrame(rs.fetchmany(5)) #escoge solo 5 primeros elementos

con.close()
print (df.head())