
import os
'''
Line 1 of comments
Line 2 of comments
Line 3 of comments
'''
os.system('clear')
#String datatype
full_name = "Srini Garlapati"

#number data type
age = 50

print(full_name + " is aged " + str(age))

# Lists
family_members = ["Srini", "Archana", "Smaran", "Smruthi"]
# Lists are indexed from 0
# family_members 0 is "Srini"

#if you just print family_members, you will get all as list
print("Now lets see how lists print")
print(family_members)
print("\n")
print(" 0-th family_members is " + family_members[0])
print("\n")

print("That was Lists in Python \n")
print("\n")
#Tuples
readonly_members = ("Laxman", "Karuna", "Sai", "Sweety")
print("Now lets see how tuples print")
print(readonly_members)
print("\n")
print(" 0-th readonly_members is " + readonly_members[0])
print("\n")
print("Lets learn Dictionary Data Type. Dictionary contains Key-Value pairs")
my_family = {
	
	"father" : "Ramulu",
	"mother" : "Suguna",
	"brother": "Laxman",
	"sister" : "Jhansi",
	"wife"	:	"Archana",
	"son"	: "Smaran",
	"daughter" : "Smruthi" 
}

print("My father is " + my_family["father"])
print("\n")
