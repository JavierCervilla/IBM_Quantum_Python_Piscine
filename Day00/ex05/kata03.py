#!/usr/bin/env python3

kata = "The right format"

def main():
    print("{kata:->42}".format(kata=kata))
    return
    
if(__name__ == '__main__'):
    main()