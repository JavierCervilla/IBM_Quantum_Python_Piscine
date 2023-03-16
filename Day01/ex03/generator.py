#!/usr/bin/env python3
from random import random
from math import floor

def fisher_yates_shuffle_improved(the_list):
    """
        fuente: https://gist.github.com/JenkinsDev/1e4bff898c72ec55df6f
    """
    amnt_to_shuffle = len(the_list)
    # We stop at 1 because anything * 0 is 0 and 0 is the first index in the list
    # so the final loop through would just cause the shuffle to place the first
    # element in... the first position, again.  This causes this shuffling
    # algorithm to run O(n-1) instead of O(n).
    while amnt_to_shuffle > 1:
        # Indice must be an integer not a float and floor returns a float
        i = int(floor(random() * amnt_to_shuffle))
        # We are using the back of the list to store the already-shuffled-indice,
        # so we will subtract by one to make sure we don't overwrite/move
        # an already shuffled element.
        amnt_to_shuffle -= 1
        # Move item from i to the front-of-the-back-of-the-list. (Catching on?)
        the_list[i], the_list[amnt_to_shuffle] = the_list[amnt_to_shuffle], the_list[i]
    return the_list

def generator(text: str, sep=" ", option=None):
    """ 
        Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
        option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
    """

    if (not isinstance(text, str) or not text.isprintable() or not isinstance(sep, str) ):
        print("ERROR")
        return
    lista = text.split(sep)
    if (option == "ordered"):
        lista.sort()

    elif (option == "unique"):
        lista = set(lista)

    elif (option == "shuffle"):
        lista = fisher_yates_shuffle_improved(lista)

    for i in lista:
        yield i

        

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
    print("\nERROR TEXT NOT STR:\n  Text:{}".format(text))
    for word in generator(text, sep=1, option="unique"):
        print(word)
    
    


    return
    
if(__name__ == '__main__'):
    main()