#!/usr/bin/env python3
import sys, string

def main():
    if (len(sys.argv) != 3):
        print("Error: Invalid number of arguments")
        return
    """ text, n = sys.argv[1], int(sys.argv[2])
    parsed = text.translate(
        str.maketrans(string.punctuation, ' ' * len(string.punctuation)) 
    )
    lista = parsed.split()
    lista = [word for word in lista if len(word) > n]
    print(lista) """
    print([ word for word in sys.argv[1].translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).split() if len(word) > int(sys.argv[2])])

if(__name__ == '__main__'):
    main()