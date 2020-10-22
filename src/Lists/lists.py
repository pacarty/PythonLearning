# Lists contain values separated by commas in square brackets

names = ['Pat', 'John', 'Rick', 'James', 'Morty']

# We can index and slice them

print(names[-1])
print(names[2:])

# We can append to a list

names.append(4)
print(names)

# We can replace certain elements during slicing
# Below, we take out incides 1 and 2 and replace them with
# whatever list we put in there. This replacement can be any size.
# If the replacement list is empty, it simply removes all elements within the specified indices.

names[1:3] = ['Ben', 'Frank', 'Adrian']
print(names)