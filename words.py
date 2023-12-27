import random

def randomGen() -> str:
    wordList = ["elkelkáposztásítottalanítottátok", "megszentségteleníthetetlenségeskedéseitekért", "eltöredezettségmentesítőtleníttethetetlenségtelenítőtlenkedhetnétek", "alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa"]
    return random.choice(wordList)

