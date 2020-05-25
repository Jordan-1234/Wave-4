def piglatin(word):
#Checks if word has vowels" 
    vowels = "aeiou"    
    
    if word[0] in vowels:
        print(word + "way")
    else:
        for i in range(len(word)):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            else:
                break
        print(word + "ay")

piglatin(str(input()))
