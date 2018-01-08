#para iter con for en pandas se debe usar interrows()
import pandas as pd 
bricks = pd.read_csv("brics.csv", index_col=0)

#iterar toda la fila
for lab,row in bricks.iterrows(): 
	print(lab )
	print(row)
	print ("\n")


#iterar toda la fila y escoge una columna
for lab,row in bricks.iterrows(): 
	print(lab,"",row["capital"])

#crear una fila
for x,y in bricks.iterrows():
	brics.loc[x,"CAPITAL"] = y["capital"].upper()
print(bricks) 