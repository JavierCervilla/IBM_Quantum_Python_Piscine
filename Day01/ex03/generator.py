#!/usr/bin/env python3
from random import random, randint
from math import floor

def generator(text: str, sep=" ", option=None):
    """ 
        Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
        option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
    """

    if (not isinstance(text, str) or not text.isprintable() or not isinstance(sep, str) ):
        print("ERROR")
        return
    words = text.split(sep)
    if option is None:
        for word in words:
            yield word
    elif option == 'shuffle':
        while len(words):
            rand = randint(0, len(words) - 1)
            yield words[rand]
            words.pop(rand)
    elif option =="unique":
        uniques = list()
        for word in words:
            if word not in uniques:
                uniques.append(word)
                yield word
    elif option == "ordered":
        while len(words):
            check = words[0]
            for word in words:
                if check > word:
                    check = word
            words.remove(check)
            yield check
    else:
        print("Not a valid option")
    return
        

def main():

    text = "Le Lorem Ipsum est simplement du faux texte."
    print("\nDEFAULT:\n  Text:{}".format(text))
    for word in generator(text, sep=" "):
        print(word)
    print("\nOPTION ORDERED:\n  Text:{}".format(text))
    for word in generator(text, sep=" ", option="ordered"):
        print(word)

    print("\nOPTION SHUFFLE:\n  Text:{}".format(text))
    for word in generator(text, sep=" ", option="unique"):
        print(word)

    text = "Lorem Ipsum Lorem Ipsum"
    print("\nOPTION UNIQUE:\n  Text:{}".format(text))
    for word in generator(text, sep=" ", option="unique"):
        print(word)

    text = 1
    print("\nERROR TEXT NOT STR:\n  Text:{}".format(text))
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    
    text = "Lorem Ipsum Lorem Ipsum"
    print("\nERROR SEP NOT STR:\n  Text:{}".format(text))
    for word in generator(text, sep=1, option="unique"):
        print(word)
    return
    
if(__name__ == '__main__'):
    main()