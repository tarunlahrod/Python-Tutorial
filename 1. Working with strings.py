# Strings

message = "hello world"

print(message)

# index
print('printing 4th index: ' + message[4])

# type: gives the type of the variable
print(type(message))

# len: length of string
print(len(message))

# Slicing: first index is inclusive and second index is exclusive
print(message[0:5])

# Methods/functions
# upper(): all letter in upper case
print(message.upper())

# count(): counts the number of appearance of a string in a string
print(message.count('l'))

# find(): finds the string in a string, if found returns index, else returns -1
print(message.find('ell'))

# replace()
message = message.replace('world', 'universe')
print(message)

# adding multiple strings and concatenating them together
firstname = 'Light'
lastname = 'Yagami'
message = firstname + ' ' + lastname
print(message)

# better approach for same task using placeholders {}
message = 'Hey, {} {}. Welcome!'.format(firstname, lastname)
print(message)

# dir(): all attribute we have access to through the variable
print(dir(firstname))

# help()
print(help(str))