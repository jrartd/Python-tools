import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

pf = pd.read_csv("Pokemon.csv", index_col=0)
sns.lmplot(x="Attack", y="Defense", data=pf,    hue="Stage",    col="Stage")
#		ejex           ejey         datos      linea			separar colores	   sparar por columnas

#plt.show()
sns.residplot(x="Attack", y="Defense", data=pf,)

plt.show()

