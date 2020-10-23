# Run a loop that prints out the letters of a name, one by one

name = "Patrick"
i = 0

while i < len(name):
    print(name[i], end='')
    i += 1

print('')

# Print out a word in a pyramid style

word = "pyramid"
i = 0

while i < len(word):
    print(word[:i + 1])
    i += 1

i = len(word)

while i > 0:
    print(word[:i])
    i -= 1
