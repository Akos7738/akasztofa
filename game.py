import random

def szar_vagy():
    exit("Szar vagy!")

def randomGen() -> str:
    wordList = ["elkelkáposztásítottalanítottátok", "megszentségteleníthetetlenségeskedéseitekért", "alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa", "tyúxar"]
    return random.choice(wordList)

word = randomGen()

wordTemplate = list()
for i in range(len(word)):
    wordTemplate.append("_")
        
print(word)
print("\nTaláld ki a megadott szót! 10 rossz válasz után vége. (betűket várok.)")

print(" ".join(wordTemplate))

while "".join(wordTemplate) != word:
    print()
    tip = input("Az ön tipje: ")
    print()

    if tip not in word:
        szar_vagy()
    else:
        for i in range(len(word)):
            if word[i] == tip:
                wordTemplate[i] = tip

    print(" ".join(wordTemplate))

print(f"Ügyes vagy, a megfejtés: {word}")
