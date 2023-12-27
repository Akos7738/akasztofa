import random
from hangmanpics import HANGMANPICS

def randomGen() -> str:
    wordList = ["elkelkáposztásítottalanítottátok", "megszentségteleníthetetlenségeskedéseitekért", "alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa"]
    return random.choice(wordList)

count = 10
word = randomGen()
used = []

wordTemplate = list()
for i in range(len(word)):
    wordTemplate.append("_")


print("\nTaláld ki a megadott szót! 10 rossz válasz után vége.")

print(" ".join(wordTemplate))

while "".join(wordTemplate) != word:
    print()
    tips = input("Az ön tipje: ").lower()
    print()

    for i in tips:
        if i not in used:
            used.append(i)
        
    for tip in tips:
        if tip not in word:
            print(HANGMANPICS[len(HANGMANPICS)-count])
            count -= 1
            if count != 0:
                print(f"Pórbálkozz újra. Még {count}x hibázhatsz.")
            else:
                print(f"A megoldás: {word}\nFelakasztottak!")
                exit()
        else:
            for i in range(len(word)):
                if word[i] == tip:
                    wordTemplate[i] = tip

    print(" ".join(wordTemplate))
    
    if used !=[]:
        print()
        print("Felhasznált betűk:", ", ".join(used))
        print()
    
if count > 0:
    print(f"Ügyes vagy, a megfejtés: {word}\nHibák száma: {10-count}")