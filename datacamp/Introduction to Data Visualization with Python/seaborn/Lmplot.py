import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("brics.csv")

sns.lmplot(x="area", y="population", data=data)
plt.show()
