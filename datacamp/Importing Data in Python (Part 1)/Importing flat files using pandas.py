#si el archivo es txt entonces usar sep= "\t", commment="#", na_values=["Nothing"]

import pandas as pd
maindata = pd.read_csv("titanic_sub.csv",index_col=1,nrows=5) #nrows analiza las filas
print (maindata["Ticket"])