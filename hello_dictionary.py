
import os

#dictionary data struct in Python holds Key-Value Pairs
fav_fruits = {
	"Srini":"Cherry",
	"Archana":"Berry",
	"Smruthi":"Mango",
	"Smaran":"Orange"
}

#What fruit does Smruthi like
print(fav_fruits["Smruthi"])
#to add more key-value pairs
fav_fruits.update({"Ramulu":"Apple"})
print(fav_fruits)

#Updating the value of a key, say Srini like banana
fav_fruits["Srini"] = "Banana";
print(fav_fruits)

#values can contain lists too
fav_fruits = {
	"Srini":["Cherry", "Kiwi", "Nectarine"],
	"Archana":"Berry",
	"Smruthi":"Mango",
	"Smaran":"Orange"
}

print(fav_fruits)
#What is srinis top fruit
print(fav_fruits["Srini"][0])