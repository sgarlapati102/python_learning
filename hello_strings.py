
import os
'''
Line 1 of comments
Line 2 of comments
Line 3 of comments
'''
os.system('clear')
#String datatype
full_name = "Srini Garlapati"

print(full_name)

full_name = "Srini Garlapati 'MS UofH'"

print(full_name)
#Srini Garlapati 'MS UofH'

full_name = "Srini Garlapati \"MS UofH\""
print(full_name)

print("Length of full_name " + str(len(full_name)))
print ("calling upper function -- " + full_name.upper())
print ("calling lower function -- " + full_name.lower())
print ("calling swapcase function -- " + full_name.swapcase())
print ("The character at 4th index is -- " + full_name[4])
print ("The characters from 0:5th index are -- " + full_name[0:5])
print("As a list using split function " )
print(full_name.split())