import pandas as pd 
tweets = pd.read_csv("../tweets.csv",index_col=0)
columnas = tweets["lang"]

vacio = {}

for tweets in columnas:
	if tweets in vacio.keys():
		vacio[tweets] += 1
	else:
		vacio[tweets] = 1
print(vacio)