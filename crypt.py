import time
import datetime


class Cryptographer:
#Change text

  def text():
    words = {
                 "a": "1*", "A": "**",
                 "b": "\s", "B": "s/",
                 "c": "*2", "C": "2_",
                 "d": "+s", "D": "-s",
                 "e": "++", "E": "+-",
                 "f": "_v", "F": "V_",
                 "g": "#@", "G": "@y",
                 "h": "#%", "H": "rr",
                 "i": "a*", "I": "fa",
                 "j": "..", "J": "--",
                 "k": "##", "K": "&#",
                 "l": "?.", "L": "</",
                 "m": "??", "M": ">>",
                 "n": "<>", "N": "^:",
                 "o": "fe", "O": "f^",
                 "p": "gd", "P": "\m",
                 "q": ";'", "Q": "_'",
                 "r": "''", "R": " -_",
                 "s": "m4", "S": "s7",
                 "t": "9h", "T": "h8",
                 "u": "\/" , "U": "/u",
                 "v": "le", "V": "zt",
                 "w": "ru", "W": "np",
                 "x": "lr", "X": "ee",
                 "y": ".e", "Y": "by",
                 "z": "p0", "Z": ".3",
                 "1": "21", "2": "02",
                 "3": "95", "4": "16",
                 "5": "25", "6": "36",
                 "7": "49", "8": "72",
                 "9": "81", "0": "99",
                 "!": "~^", "?": "~~",
                 ".": "+_", ",": "*~",
                 " ": "||", ":": "|:",
                 '"': ",|", "'": "@|",
                 "@": "@@", "%": "~-",
                 "(": "))", ")": "()",
                 "+": "10", "-": "00",
                 "*": "11", "<": "22",
                 ">": "23", "$": "79"
                 }
    return words

  def cipher(strong):
    word = ""
    words = Cryptographer.text()
    for i in strong:
        if i in words:
            word += str(words[i])
    return word

#Return text    

  def decryption(strong):
    if len(strong)%2 != 0:
        return "I can't work with it. Try again"
    else:
        text_word = ""
        words = Cryptographer.back_cipher()
        pos1 = 0
        pos2 = 1
        while True:
            if strong[pos1:pos2 + 1] in words:
                text_word += words[strong[pos1:pos2 + 1]]
            else:
                return "I can't work with it. Try again2"
            if pos1 + 2 < len(strong) and pos2 + 2 <= len(strong):
                pos1 += 2
                pos2 += 2
            else:
                return text_word
  

  def back_cipher():
    back_words = {'1*': 'a', '**': 'A',
                  '\s': 'b', 's/': 'B',
                  '*2': 'c', '2_': 'C',
                  '+s': 'd', '-s': 'D',
                  '++': 'e', '+-': 'E',
                  '_v': 'f', 'V_': 'F',
                  '#@': 'g', '@y': 'G',
                  '#%': 'h', 'rr': 'H',
                  'a*': 'i', 'fa': 'I',
                  '..': 'j', '--': 'J',
                  '##': 'k', '&#': 'K',
                  '?.': 'l', '</': 'L',
                  '??': 'm', '>>': 'M',
                  '<>': 'n', '^:': 'N',
                  'fe': 'o', 'f^': 'O',
                  'gd': 'p', '\m': 'P',
                  ";'": 'q', "_'": 'Q',
                  "''": 'r', '-_': 'R',
                  'm4': 's', 's7': 'S',
                  '9h': 't', 'h8': 'T',
                  '\/': 'u', '/u': 'U',
                  'le': 'v', 'zt': 'V',
                  'ru': 'w', 'np': 'W',
                  'lr': 'x', 'ee': 'X',
                  '.e': 'y', 'by': 'Y',
                  'p0': 'z', '.3': 'Z',
                  '21': '1', '02': '2',
                  '95': '3', '16': '4',
                  '25': '5', '36': '6',
                  '49': '7', '72': '8',
                  '81': '9', '99': '0',
                  '~^': '!', '~~': '?',
                  '+_': '.', '*~': ',',
                  '||': ' ', '|:': ':',
                  ',|': '"', '@|': "'",
                  '@@': '@', '~-': '%',
                  '))': '(', '()': ')',
                  '10': '+', '00': '-',
                  '11': '*', '22': '<',
                  '23': '>', '79': '$'}
    
    return back_words  
#Test


while True:
    num = int(input("1. Encrypt\n2. Decipher\n"))
    stronger = input("Enter:\n")
    if num == 1:
        stronger = Cryptographer.cipher(stronger)
        print(stronger)
        time.sleep(0.8)
        print("Want to go back to the beginning?")
        xs = int(input("1. Yes\n2. No\n"))
        if xs == 2:
            break
    elif num == 2:
        stronger = Cryptographer.decryption(stronger)
        print(stronger)
        print("Want to go back to the beginning?")
        xs = int(input("1. Yes\n2. No\n"))
        if xs == 2:
            break
        else:
            print("Try again")
  

    
  
  