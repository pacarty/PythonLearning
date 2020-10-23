# if a statement is true, execute everything after the if statement
# if false, move on to next elif until you get to "else",
# in which case execute that statement.
# if there is no "else" or "elif" simply do nothing.

num = 55

if num >= 60:
    print('Its higher than 60')
elif num >= 50 and num < 60:
    print('Its between 50 and 59')
else:
    print('Its below 50')

