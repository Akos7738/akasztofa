import random

def randomGen() -> str:
    wordList = ["elkelkáposztásítottalanítottátok", "megszentségteleníthetetlenségeskedéseitekért", "alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa"]
    return random.choice(wordList)

count = 10
word = randomGen()

wordTemplate = list()
for i in range(len(word)):
    wordTemplate.append("_")
        
print(word)
print("\nTaláld ki a megadott szót! 10 rossz válasz után vége. (kis betűket várok.)")

print(" ".join(wordTemplate))

while "".join(wordTemplate) != word:
    print()
    tip = input("Az ön tipje: ")
    print()

    if tip not in word:
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
if count > 0:
    print(f"Ügyes vagy, a megfejtés: {word}\nHibák száma: {10-count}")