#!/usr/bin/env python3

kata = (12, 15, 18)

def main():
    print("The {length} numbers are: {numbers}".format(length = str(len(kata)), numbers = ", ".join(str(number) for number in kata)))
    return
    
if(__name__ == '__main__'):
    main()