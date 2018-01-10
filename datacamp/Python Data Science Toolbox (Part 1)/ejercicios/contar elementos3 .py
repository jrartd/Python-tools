import pandas as pd 
tweets = pd.read_csv("../tweets.csv",index_col=0)
coltweets=tweets["lang"]

resultado = {}

for items in coltweets:
	if items in resultado.keys():
		resultado[items] += 1
	else:
		resultado[items]= 1

print(resultado) 