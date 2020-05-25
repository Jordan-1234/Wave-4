# Write a function named reverseLookup that finds all of the keys in a dictionary
# that map to a specific value. The function will take the dictionary and the value to
# search for as its only parameters. It will return a (possibly empty) list of keys from
# the dictionary that map to the provided value.
# Your program should create a dictionary and then
# show that the reverseLookup function works correctly when it returns multiple
# keys, a single key, and no keys.


def reverse_lookup(dictionary, value):


keys = []
   for key in dictionary:
        if dictionary[key] == value:
            keys.apprend(key)
    return(keys)


def practice()
    names_and_ages = ["John": "15", "John" : "13", "Mary" : "3", "Caleb" : "100"]
       print("The peoples names are: ", reverse_lookup(names_and_ages, "John"))
        print()
