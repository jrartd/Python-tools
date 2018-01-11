cambio = lambda x,y : print(x + y) #lambda funciones anonimas
#variable=lambda parametro1,parametro2 : ___lo que deseamos ejecutar___
cambio(1,2)
print (cambio)

#_____________________________________________________________________________________

#map me permite iterar sobre todos los elemntos de una lista
nums= [2,4,6,7,8,3,4]
funciones = map(lambda nums: nums *2,nums)
#variable = map(lambda,lista o parametros : __lo que deseamos ejecutar__,llamamos la funcion)
print(list(funciones))

#MAP_____________________________________________________________________________________
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda spells: spells + "!!!",spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)

#FILTER _____________________________________________________________________________________

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member : len(member) > 6,fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)


#REDUCE _____________________________________________________________________________________
# Import reduce from functools
from functools import reduce 

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2 : item1 + item2 , stark)

# Print the result
print(result)
