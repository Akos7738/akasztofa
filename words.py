import random

def randomGen() -> str:
    rawText = list()
    words = list()

    with open("./kisherceg.txt", "r", encoding="utf-8") as text:
        rawText = text.readlines()
    
#print(rawText)

    textContent = list()
    for line in rawText:
        textContent.append(line.strip().replace("-","").replace(".","").replace(",","").replace("!","").replace("?","").replace(";","").replace(":","").replace("'","").replace('"','').replace("˝","").replace("´","").replace("”","").replace("(","").replace(")","").replace("„",""))
    
    for line in textContent:
        tempLine = line.split(" ")
        for w in line.split():
            if len(w) > 3:
                words.append(w)
#print(words)
    return(random.choice(words))
