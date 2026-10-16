import config
import pifinder
## other files working together

import mpmath
## external libraries

conversions = {
    "00": " ",
    "01": "A",
    "02": "B",
    "03": "C",
    "04": "D",
    "05": "E",
    "06": "F",
    "07": "G",
    "08": "H",
    "09": "I",
    "10": "J",
    "11": "K",
    "12": "L",
    "13": "M",
    "14": "N",
    "15": "O",
    "16": "P",
    "17": "Q",
    "18": "R",
    "19": "S",
    "20": "T",
    "21": "U",
    "22": "V",
    "23": "W",
    "24": "X",
    "25": "X",
    "26": "Z",
    ## ughhhhh there was definitely a better method but i lowk could not be bothered
}

def splice(pidigits, pistring):
    pistring = pistring.replace(".","")

    processed = []

    for x in range(0,len(pistring) - 1,2):
        comb = pistring[x : x+2]
