
import os
'''
Line 1 of comments
Line 2 of comments
Line 3 of comments
'''
#Tuples are just like lists but immutable
#sample tuple, only difference from list is ()
namesTuple = ("Srini", "Archana", "Smaran", "Smruthi")

print(namesTuple)

print("how many items in my tuple")
print(len(namesTuple))
#Lists start with 0 index
print("what is the second item in my tuple")
print(namesTuple[1])

#Tuples are immutable. To add items, create a new tuple and add


#Another tuple
parentsTuple = ("Ramulu","Suguna")
print( parentsTuple)

#Add the Tuples
all_namesTuple = namesTuple + parentsTuple
print(all_namesTuple)

#if you need to remove items from Tuple, create new own and use range etc

all_names_truncatedT = all_namesTuple[0:2]
print(all_names_truncatedT)


