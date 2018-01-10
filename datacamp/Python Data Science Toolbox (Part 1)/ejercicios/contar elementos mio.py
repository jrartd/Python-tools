import pandas as pd
maindata = pd.read_csv("../tweets.csv")

#crear dicionario

dic = {} 					#selecciono el dicionario donde ira la info
col = maindata["lang"] 		#selecciono la 

for x in col: 				#iterar cada registro
	if x in dic.keys():		#selecciono el indice a contar
		dic[x] += 1
	else:
		dic[x] = 1

print(dic) 

