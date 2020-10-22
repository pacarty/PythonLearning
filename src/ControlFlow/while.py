# Print numbers one by one

count = 0

while count < 5:
    print(count)
    count += 1

# We can use the argument "end" to add text to the end of
# each print statement instead of starting a new line each time

count = 0

while count < 5:
    print(count, end=', ')
    count += 1

print(count)