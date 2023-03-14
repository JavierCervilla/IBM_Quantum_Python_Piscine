#!/usr/bin/env python3
import sys

# 10 + 9 + 8 + ... + 0
def func():
    for i in range(0,11):
        if (i == 0):
            y = 0
        y += i
        yield y
        

def main():
    for x in func():
        print(x)
    return
    
if(__name__ == '__main__'):
    main()