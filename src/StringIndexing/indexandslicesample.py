# This program contains some strings which are ID numbers.
# The ID numbers are in a format where the first char is a "Group ID", the next 3 are
# "Area Code", and the last 4 digits are "Personal ID"
# We want to separate all these into their own values

person1 = '3972-2845'
person2 = '4972-1948'

person1GroupID = person1[0]
person2GroupID = person2[0]

person1AreaCode = person1[1:4]
person2AreaCode = person2[1:4]

person1PersonalID = person1[-4:]
person2PersonalID = person2[-4:]

print('Person 1')
print('GroupID:', person1GroupID)
print('Area Code:', person1AreaCode)
print('PersonalID', person1PersonalID)

print('Person 2')
print('GroupID:', person2GroupID)
print('Area Code:', person2AreaCode)
print('PersonalID', person2PersonalID)