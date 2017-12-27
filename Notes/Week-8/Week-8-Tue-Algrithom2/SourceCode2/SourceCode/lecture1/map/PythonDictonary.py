dict = {'Name': 'Alice', 'Age': 7, 'Class': 'First'}

print ("Name: ", dict['Name'])
print ("Age: ", dict['Age'])
print(dict)

# KeyError: 'Sex'
# print ("Sex: ", dict['Sex'])

print("\nUpdating Dictionary")
dict['Age'] = 8; # update existing entry
dict['Sex'] = 'F'; # update existing entry
dict['School'] = "Elementary School"; # Add new entry
print ("Name: ", dict['Name'])
print ("Age: ", dict['Age'])
print ("Sex: ", dict['Sex'])
print(dict)

print("\nDelete Dictionary Elements")
del dict['Name']; # remove entry with key 'Name'
print(dict)
# KeyError: 'Name'
# print ("Name: ", dict['Name'])
dict.clear();     # remove all entries in dict
print(dict)
# KeyError: 'Sex'
#print ("Sex: ", dict['Sex'])
del dict ;        # delete entire dictionary
print(dict)


print("\nProperties of Dictionary Keys")
print("\n  1. More than one entry per key not allowed")
dict = {'Name': 'Alice', 'Age': 7, 'Class': 'First', 'Age': 8}
print(dict)

print("\n  2. Keys must be immutable")
# TypeError: unhashable type: 'list'
dict = {['Name']: 'Zara', 'Age': 7}
print ("dict['Name']: ", dict['Name'])



a = "abc"
b = "xyz"

dict[a] = 123
dict[b] = 456
