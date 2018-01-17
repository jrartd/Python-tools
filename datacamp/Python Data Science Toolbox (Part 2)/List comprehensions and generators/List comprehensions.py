#for normal
nums = [2,4,5,7,8,8]
new = []

for value in nums:
	new.append(value + 1)

print (new)

#for comprimido
dos = [2,4,5,7,8,8]
tres = [h + 3 for h in dos]
print(tres)

#con range
cinco = [j + 1 for j in range (11)]
print(cinco)


holap = [jk + 4 for jk in range (25)]
print(holap)

# Create list comprehension: squares
squares = [i**2 for i in range(0,10)]
print(squares)


# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range (5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)





# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)




# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new list
print(new_fellowship)
