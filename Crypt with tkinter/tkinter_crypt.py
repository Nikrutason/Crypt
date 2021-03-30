import time
import datetime
import os
import tkinter as tk
from tkinter import messagebox as mbx
global name
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


  def cipher():
    strong = name.get()
    word = ""
    words = Cryptographer.text()
    for i in strong:
        if i in words:
            word += str(words[i])
        else:
            return mbx.showerror("Error", "Try again")
    trans = tk.Label(window, text="Your new text:", font=("Arial black", 16))
    trans.grid(column=0, row=3)
    trans_txt =tk.Entry(window, font=("Arial", 14), width=100)
    trans_txt.grid(column=1, row=3, stick="w")
    trans_txt.insert(0, word)
#Return text    
  def decryption():
    dest = name2.get()
    if len(dest)%2 != 0:
      return mbx.showerror("Error", "Try again")
    else:
        text_word = ""
        words = Cryptographer.back_cipher()
        pos1 = 0
        pos2 = 1
        while True:
            if dest[pos1:pos2 + 1] in words:
                text_word += words[dest[pos1:pos2 + 1]]
            else:
                return mbx.showerror("Error", "Try again")
            if pos1 + 2 < len(dest) and pos2 + 2 <= len(dest):
                pos1 += 2
                pos2 += 2
            else:
                trans = tk.Label(window2, text="Your new text:", font=("Arial black", 16))
                trans.grid(column=0, row=3)
                trans_txt = tk.Entry(window2, font=("Arial", 14),width=100)
                trans_txt.grid(column=1, row=3, stick="w")
                trans_txt.insert(0, text_word)
                break
  
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
#Function for buttons
#Text Back

def comptany():
    global name2, window2
    window2 = tk.Tk()
    window2.geometry("580x200+10+10")
    text_phrase = tk.Label(window2, text="Enter your text:",
                           font=("Arial black", 15))
    text_phrase.grid(column=0, row=0)
    name2 = tk.Entry(window2, width=100, font=("Arial", 15))
    name2.grid(column=1, row=0)
    bow = tk.Button(window2, text="Translate", font=("Arial black", 12),
                    command=Cryptographer.decryption)
    bow.grid(column=0, row=1, stick="e")

    window2.mainloop()
#Test in crypt


def compt():
    global name, window
    window = tk.Tk()
    window.geometry("580x200+10+10")
    text_phrase = tk.Label(window, text="Enter your text:",
                           font=("Arial black", 15))
    text_phrase.grid(column=0, row=0)
    name = tk.Entry(window, width=100, font=("Arial", 15))
    name.grid(column=1, row=0)
    bow = tk.Button(window, text="Translate", font=("Arial black", 12),
                    command=Cryptographer.cipher)
    bow.grid(column=0, row=1, stick="e")
    window.mainloop()

#Menu


win = tk.Tk()
win.title("Cryptographer")
win.geometry("580x150+500+215")
win.resizable(False, False)
btn = tk.Button(win, text="Encrypt",
                command=compt,
                width=10, height=2,
                font=("Arial black", 30))
btn.grid(column=0, row=0)
btn = tk.Button(win, text="Decipher",
                width=10, height=2,
                font=("Arial black", 30),
                command=comptany)
btn.grid(column=1, row=0)
win.mainloop()