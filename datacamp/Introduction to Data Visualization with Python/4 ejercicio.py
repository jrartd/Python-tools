import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
physical_sciences = data[["Physical Sciences"]]
computer_science = data[["Computer Science"]]
year = data[["Year"]]
health = data[["Health Professions"]]
education = data[["Education"]]

# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year,physical_sciences , color='blue', label="physical_sciences")
plt.title('Physical Sciences')
plt.legend(loc="upper right")
# Make the top right subplot active in the current 2x2 subplot grid 
plt.subplot(2,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red', label="computer_science")
plt.title('Computer Science')
plt.legend(loc="upper right")
# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2,2,3)

# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green',label="Health")
plt.title('Health Professions')
plt.legend(loc="upper right")
# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,4)

# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='yellow',label="Education")
plt.title('Education')

# Improve the spacing between subplots and display them
plt.legend(loc="upper right")
plt.tight_layout()

plt.annotate("jorge", xy=(0.5,0.8))


plt.show()
#guardar imagen
plt.savefig("xlim_and_ylim.png")
