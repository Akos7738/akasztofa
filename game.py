import random

def randomGen() -> str:
    wordList = ["elkelkáposztásítottalanítottátok", "megszentségteleníthetetlenségeskedéseitekért", "alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa"]
    return random.choice(wordList)

wordTemplate = list()

word = randomGen()

print(word)

for i in range(len(word)):
    wordTemplate.append("_")

print()
print(" ".join(wordTemplate))

print("\nTaláld ki a megadott szót! 10 rossz válasz után vége. (betűket várok.)")
tip = input("Az ön tipje: ")

if tip not in word:
    print("Szar vagy!")
else:
    for i in range(len(word)):
        if word[i] == tip:
            wordTemplate[i] = tip

print(" ".join(wordTemplate))