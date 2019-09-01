# Lists
animes = ['ReZero', 'Death Note', 'Steins Gate', 'Your lie in April']
print('Print all elements in the list: ', animes)
print("Length of list = ", len(animes))
print('Last element: ', animes[3])

# last element can be gained by -1
print('Printing last element using "-1" index: ', animes[-1])

# Slicing
# accessing a range of values
	# first index is INCLUSIVE and second index is EXCLUSIVE
print('\nSlicing:')
print(animes[0:2])
print(animes[:2])
print(animes[1:])


# List methods
print('\nList methods:')
	# Adding an item to a list
animes.append('Boku no Hero Academia')
print('\nUsing append method: ', animes)

	# to insert at a particular index
animes.insert(0, 'Tokyo Ghoul')
print('\nUsing insert method: ', animes)

	# to add multiple values to a list (or to add another list to an existing list)
anime_list2 = ['One Punch Man', 'Mob Psycho 100']
# uncomment the line below
# animes.insert(0, anime_list2)
print('\n\nMerged Lists: ', animes)

print('\nThe value at first index of animes list is itself a list: ', animes[0])

	# to overcome this issue, we use extend method
		# commenting the line number 32 (animes.insert....)
animes.extend(anime_list2)
print('\nExtended list: ', animes)


# Removing
print('\n\nRemoving values from a list')
animes.remove('Tokyo Ghoul')
print('\nAfter removing "Tokyo Ghoul": ', animes)

	# pop method: removes the last element of the list
	# used to act as stack and queue
	# returns the popped element
popped = animes.pop()
print('\nPopped element: ', popped)

# Reversing a list
animes.reverse()
print('\nReversing the list: ', animes)

# Sorting a list
animes.sort()
print('\nSorted the list: ', animes)
	
	# for reversed sort (descending order)
animes.sort(reverse=True)
print('\nSorted the list (descending): ', animes)

# If we do not want the current list to be sorted instead just
# want to store the sorted list in a new list and this list 
# remain intact

animes = ['ReZero', 'Death Note', 'Steins Gate', 'Your lie in April']

# for this, we use sorted() function
sorted_animes = sorted(animes)
print('\nAnimes list (remain unsorted): ', animes)
print('\nAnimes sorted list: ', sorted_animes)


# Min, Max and Sum
num = [1, 4, 2, 5, 3]
print('\n\nMin: ', min(num))
print('Max: ', max(num))
print('Sum: ', sum(num))


# To find an index by its value (if value doesn't exists in the list, we'll get an error)
print('\nThe index of "Your lie in April" is: ', animes.index('Your lie in April'))

# To check if a value is in our list
print('\nCheck if "ReZero" is in the list: ', 'ReZero' in animes)

# A for loop
for anime in animes:
	print(anime)

# To access the index as well
# We use enumerate function
# It returns index and value both
print('\n')
for index, anime in enumerate(animes):
	print(index, anime)

# To start from some index
print('\n')
for index, anime in enumerate(animes, start = 1):
	print(index, anime)

# Converting our list into strings
	# We use string method called "join" 
animes_str = ', '.join(animes)
print('\nString version of our list: ', animes_str)

# Converting a string to list
	# We use "split" function for this
new_list = animes_str.split(' - ')
print('\nString version of Anime list: ', animes_str)
print('\nList version of Anime list to string: ', new_list)