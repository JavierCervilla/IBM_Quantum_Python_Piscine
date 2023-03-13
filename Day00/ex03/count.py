#!/usr/bin/env python3
import string, sys


def text_analyzer(*arg):
    """
@description: This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
@params: string(optional)
@return: void
"""
    upper,lower,punct,spaces,text_len = 0,0,0,0, 0
    try:
        if (len(arg) == 0):
            text_to_analyze = input("What is the text to analyze?")
        else:
            text_to_analyze = arg[0]
        if (type(text_to_analyze) != str):
            raise TypeError
        for letter in text_to_analyze:
            if (letter.isupper()): upper += 1
            elif (letter.islower()): lower += 1
            elif (letter.isspace()): spaces += 1
            elif (letter in string.punctuation): punct += 1
            text_len += 1
        text="The text contains {text_len} character(s):\n - {upper} upper letter(s)\n - {lower} lower letter(s)\n - {punct} punctuation mark(s)\n - {spaces} space(s)".format(text_len=text_len, upper=upper, lower=lower, punct=punct, spaces=spaces)
        print(text)
    except:
        print("AssertionError: argument is not a string is " + str(type(text_to_analyze)))

def main():
    """
@description: This program is a text analyzer.
"""
    try:
        if (len(sys.argv) > 2):
            raise TypeError
        elif (len(sys.argv) == 2):
            text_analyzer(sys.argv[1])
        else:
            text_analyzer()
        return;
    except:
        print("Error: Multiple Arguments, Usage: python3 count.py <text>")
        return
if(__name__ == '__main__'):
    main()