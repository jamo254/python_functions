#lists 
import re
import datetime
names = ["Ubri", "Joe", "Andrey", "Petre"]
print(type(names))
# Dictionaries   (<key>, <value>)
#Russian football league

russian_league = {
    "Moscow" : "CSKA",
    "Petersburg" : "Zannit",
    "Kransnador": "Lokomotive",
    "Sochi" : "Sochi Fc"
}

# Add items 
russian_league["Belgrod"] = "Ubri FC"



#Access change data using keys
russian_league["Moscow"] = "Spatan FC"

# print("Updating league table: ", russian_league)

#Accessing items using keys
print(russian_league["Moscow"])

#Print out teams located in Sochi and Kransnador using keys

#Removing items from a Dictionary
del russian_league["Sochi"]

print("Updated table: ", russian_league)

#Checking whether records exist

print("Socho" in russian_league)

def check_records(league):
    if "Moscoww" in league:
        return league
    else:
        return "Record does not exit"

checking = check_records(russian_league)
# print(checking)
 
#Accessing items using values
dictionary_values = russian_league.values()
print("Values = ", dictionary_values) 

#Using update to modify items

russian_league.update({"Sochi": "NFT FC"}) 
print(russian_league) 

#How to delete all items -> clear()

#Using for loop with dict

for key in russian_league:
    if key == "Moscowa":
        print("You won a new car")

