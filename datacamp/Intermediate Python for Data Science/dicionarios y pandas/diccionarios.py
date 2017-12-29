world={"ecuador":"quito"}
print (world)
world["colombia"]="bogota" # con esto se suma 
del(world["ecuador"]) # borra 
print (world)


"""
Para iterar un dicionario se usa
for x,y in variable.items():  --> todo el diccionario
for x in variable.keys()
for x in variable.values()
"""
#___________________________________________________________________

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe["italy"]= "rome"

# Print out italy in europe
print (europe)

# Add poland to europe
europe["poland"] = "warsaw"

# Print europe
print (europe)


#___________________________________________________________________

#IMPRIMIR DICCIONARIOS DENTRO DE DICCIONARIOS
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print (europe["france"]["capital"])

#___________________________________________________________________

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print (europe["france"]["capital"])

# crea una variable diccionario para poder incluir luego
data ={"capital":"rome","population": 59.83}

# Añadir el dicionario ante creado a el diccionario principal
europe["italy"]= data

# Print europe
print (europe)