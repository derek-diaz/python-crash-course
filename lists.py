# Lists are just like arrays!

some_list = ["One", "Two", "Three"]

# Lists are base 0
print(some_list[0])  # Should be One

# Giving a negative value will start from the back
print(some_list[-1])  # Should be Three
print(some_list[-2])  # Should be Two

# Length of the list
print(len(some_list))

# Adds the value a the end
some_list.append("Four")
print(some_list[-1])

some_list.insert(1, "Some number")
del some_list[1]

# get the last element
pop = some_list.pop()

# Should say Four
print(pop)

# Print List
print(some_list)

# Remove by value
some_list.remove("Two")
print(some_list)



# Sorting
