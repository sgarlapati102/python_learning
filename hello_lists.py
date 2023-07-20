
import os
'''
Line 1 of comments
Line 2 of comments
Line 3 of comments
'''
#sample list
names = ["Srini", "Archana", "Smaran", "Smruthi"]

print(names)

print("how many items in my list")
print(len(names))
#Lists start with 0 index
print("what is the second item in my list")
print(names[1])

#Lists can contain other lists
parents = ["Ramulu","Suguna"]
print( parents)
all_names = [names, parents]
print(all_names)
print("Who is the first parent")
print(all_names[1][0])

##adding items to list
all_names.append("Mohan")
print(all_names)