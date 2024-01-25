import random
from hangmanpics import HANGMANPICS
from words import randomGen

lives = 10
word = randomGen()
used = []

wordTemplate = list()
for i in range(len(word)):
    wordTemplate.append("_")


print("\nTaláld ki a megadott szót! 10 rossz válasz után vége.")
print(word)
print(" ".join(wordTemplate))

while "".join(wordTemplate) != word:
    print()
    tips = input("Az ön tipje: ").lower()
    print()

    for tip in tips:
        if tip not in used:
            used.append(tip)
            if tip not in word:
                print(HANGMANPICS[len(HANGMANPICS) - lives])
                lives -= 1
                if lives != 0:
                    print(f"Pórbálkozz újra. Még {lives}x hibázhatsz.")
                else:
                    print(f"A megoldás: {word}\nFelakasztottak!")
                    exit()
            else:
                for i in range(len(word)):
                    if word[i] == tip:
                        wordTemplate[i] = tip
        else:
            print("Ezt már próbáltad!")

    print(" ".join(wordTemplate))
    
    if used !=[]:
        print()
        print("Felhasznált betűk:", ", ".join(used))
        print()
    
if lives > 0:
    points = 10 - lives
    
    print(f"Ügyes vagy, a megfejtés: {word}\nHibák száma: {points}\n{len(used)} betűt használtál.")
    
    if points == 0:
        print("\nArany érmet kaptál!")
    elif points in range(1, 4):
        print("\nEzüst érmet kaptál!")
    elif points in range(4, 7):
        print("\nBronz érmet kaptál!")
    elif points in range(7, 10):
        print("\nNem  kaptál érmet!")

input("nyomj ENTER - t a kilépéshez")
