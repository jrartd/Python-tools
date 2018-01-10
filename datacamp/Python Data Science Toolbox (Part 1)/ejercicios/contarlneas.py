import pandas as pd
data = pd.read_csv("../tweets.csv",index_col=0)

columna = data["lang"]
selecol = (columna == "et" )

print(data[selecol])
print(data.shape)