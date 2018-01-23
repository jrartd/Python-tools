import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

plt.figure(figsize=(10,6))

#datos
data = pd.read_csv("pokemon.csv")
plt.ylim(0, 160)
sns.lmplot(x="Attack", y="Defense" , data=data, hue="Stage")
#sns.swarmplot(x="Type 1", y="Attack", dodge=True, data=data, hue="Type 1", color="black")
#sns.violinplot(x='Type 1', y='Attack', data=data, alpha=0.5, inner=None)
#sns.swarmplot(x='Stat', y='value', data=data, hue='Type 1')
plt.grid()
plt.show()