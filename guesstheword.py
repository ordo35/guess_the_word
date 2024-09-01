import random

words = ["turkiye","izmir","cesme","fenerbahce"]
word = random.choice(words)

guesses = []

gamefinish = False

print("_ "*len(word))

while not gamefinish:
    guess = input("enter a letter for guess:")
    guesses.append(guess)

    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print("")

    



            
            


    