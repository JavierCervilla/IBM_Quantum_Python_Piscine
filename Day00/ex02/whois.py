#!/usr/bin/env python3
import sys
 
def main():
    if (len(sys.argv) != 2 or sys.argv[1].isnumeric() == False):
        print ("Error: Usage: python3 whois.py <number>")
        return
    messages = ("I`m Even", "I`m Odd", "I`m Zero")
    num = int(sys.argv[1])
    if (num == 0):
        print(messages[2])
        exit()
    print(messages[num % 2])
    
if(__name__ == '__main__'):
    main()