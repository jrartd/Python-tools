import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
physical_sciences = data[["Physical Sciences"]]
computer_science = data[["Computer Science"]]
year = data[["Year"]]
# Create plot axes for the first line plot
plt.axes([0.05,0.05,0.425,0.9])

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Create plot axes for the second line plot
plt.axes([0.525, 0.05, 0.425, 0.9])

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.annotate("jorge", xy=(0.05,0.0), xytext=(3, 1.5))

plt.tight_layout() #ajusta el tamaño de los subplots
plt.show()
