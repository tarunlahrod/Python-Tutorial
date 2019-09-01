# working with numeric data

num = 3
print(type(num))

num = 3.14
print(type(num))

# Arithmatic Operations:

# Addition:			3 + 2
# Subtraction:		3 - 2
# Multiplication:	3 * 2
# Division: 		3 / 2
# Floor Division:	3 // 2
# Exponent:			3 ** 2
# Modulus:			3 % 2

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)

# incrementing
num = 1
num = num + 1
print('num: ', num)

# shorthand for incrementing
num += 1
print('num (shorthand): ', num)

# built-in functions
# abs()
print('absolute value of -1 = ', abs(-1))

# round()
print('rounded value of 3.14 = ', round(3.14))
print('round value to first digit after the decimal = ', round(3.75, 1))

# Comparison Operators:
print("\n\nComparison Operators:\n")
print('Equal:				', 3 == 2)
print('Not Equal:			', 3 != 2)
print('Greater Than:		', 3 > 2)
print('Less Than:			', 3 < 2)
print('Greater or Equal:	', 3 >= 2)
print('Less or Equal:		', 3 <= 2)

# Nums and Strings
num_1 = '100'
num_2 = '200'

# now we want to add these two values
print('Since these are strings, so + (plus operator) will concatenate them as: ' + num_1 + num_2)

# to add the we use what we call as data type casting
num_1 = int(num_1)
num_2 = int(num_2)

print('num_1 + num_2 = ', num_1 + num_2)
