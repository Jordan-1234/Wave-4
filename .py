def reverse_lookup(dictionary, value):
    keys = []
    for key in dictionary:
        if dictionary[key] == value:
            keys.apprend(key)
    return keys

    names = {
        "John": "Dog",
        "John": "Cat",
        "Mary": "Lizard",
        "Caleb": "Rat"
    }
    print("The peoples names are: ", reverse_lookup(names, "John"))
    print()
