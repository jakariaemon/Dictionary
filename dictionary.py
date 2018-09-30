# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 06:03:37 2018

@author: Emon
"""
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

from tkinter import * 

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
    
    
def click():
    word = textentry.get()
    output.delete(0.0,END)
    de = translate(word)
    if type(de) == list:
        for item in de:
             output.insert(END,item)
    else:
        output.insert(END,de)
    
    

window = Tk()
window.title("Dictionary")



Label(window, text="Enter the word you would like a defination for:",fg="Blue", font="none 12 bold").grid(row=1,column=0,sticky=W)
textentry = Entry(window, width=20)
textentry.grid(row=2, column=0, sticky=W)

Button(window, text="Submit", width=6, command=click).grid(row=3,column=0,sticky=W)

Label(window, text="\nDefinition",fg="Red", font="none 12 bold").grid(row=4,column=0,sticky=W)
output =Text(window, width=80, height=6, wrap=WORD)
output.grid(row=5, column=0, columnspan=2, sticky=W)
window.mainloop()
