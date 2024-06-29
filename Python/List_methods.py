# List methods
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# append() - Adds an item to the end of the list
li.append(11)
print(li)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# copy() - Returns a shallow copy of the list
new_list = li.copy()
print(new_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# count() - Returns the count of occurrences of a value
count_11 = li.count(11)
print(count_11)  # Output: 1

# extend() - Extends the list by appending elements from another iterable
li.extend([12, 13])
print(li)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# index() - Returns the index of the first occurrence of a value
index_of_5 = li.index(5)
print(index_of_5)  # Output: 4

# insert() - Inserts an item at a given position
li.insert(0, 0)  # Inserts 0 at index 0
print(li)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# pop() - Removes and returns the item at the given position (default is the last item)
popped_item = li.pop()
print(popped_item)  # Output: 13
print(li)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# remove() - Removes the first occurrence of a value
li.remove(0)
print(li)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# reverse() - Reverses the list in place
li.reverse()
print(li)  # Output: [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# sort() - Sorts the list in ascending order by default
li.sort()
print(li)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# clear() - Removes all items from the list
li.clear()
print(li)  # Output: []
