def piglatin(word):
    vowels = "aeiou"    
    number = "1234567890"

    if word[0] in vowels:
        print(word + "way")
    elif word[0] not in number:
        print(word[1:] + word[0] + "ay")

piglatin(str(input()))