# We can slice a string into a separate substring

name = 'Patrick'

# Slicing includes the first index and excludes the last

print(name[0:3])
print(name[3:7])

# Leaving the first index blank means the first index is 0 by default.
# Leaving the second index blank means the second index is the size  of the
# string by default
print(name[:3])
print(name[3:])

# The same rules apply to negative indices.

# Here we simply start at n-4 and then finish at n-1 (the last index)
print(name[-4:])

# Here we start at 0 and finish at the index before n-4
print(name[:-4])