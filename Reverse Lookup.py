def reverse_lookup(dictionary, value):
    keys = []
    for key in dictionary.keys():
        if dictionary[key] == value:
            keys.append(key)
    return keys

animal_Names = {"John": "Dog", "Jordan": "Dog","Mary": "Lizard", "Caleb": "Rat"}
#Prints out multiple keys
print("The names are: ", reverse_lookup(animal_Names, "Dog"))
#Prints out a single keys
print("The names are: ", reverse_lookup(animal_Names, "Lizard"))
#Prints out no keys
print("The names are: ", reverse_lookup(animal_Names, "Tiger"))
