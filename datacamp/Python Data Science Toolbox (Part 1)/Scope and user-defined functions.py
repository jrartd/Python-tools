"""
Scope = la parte de un programa donde un objeto o nombre es acesible

gloabl = definidas en el cuerpo
local = definida dentro de una función
built-in scope = nombradas predefinidas dentro del modulo

"""

# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team  #la forma de cambiar una variable de

    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)
