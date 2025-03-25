# Creatin a list
my_list = []

# Appending
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at second position
my_list.insert(1, 15)

# Extending
my_list.extend([50, 60, 70])

# Removing
my_list.pop()

# sorting
my_list.sort()

# finding & printing
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# print the final list
print("Final list:", my_list)