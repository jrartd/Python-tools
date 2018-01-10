import pandas as pd 
informacion = pd.read_csv("../tweets.csv",index_col=0)

columnainf = informacion["lang"]
resultado = {}

for idiomas in columnainf:
	if idiomas in resultado.keys():
		resultado[idiomas] += 1
	else:
		resultado[idiomas] = 1

print(resultado) 