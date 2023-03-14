#!/usr/bin/env python3

from random import randint

class Game:
    def __init__(self):
        self.__number = randint(1,99);
        print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit'to end the game.\nGood luck!")
        self.guess()

    def guess(self):
        while True:
            print("What's your guess between 1 and 99?")
            aux = input(">> ")
            if (aux == 'exit'):
                print("Goodbye!")
                return
            elif (aux.isnumeric() == False):
                print("That's not a number.\n")
            elif (int(aux) < 1 or int(aux) > 99):
                print("Out of range.\n")
            elif (int(aux) < self.__number):
                print("Too low!\n")
            elif (int(aux) > self.__number):
                print("Too high!\n")
            else:
                print("Congratulations, you've got it!")
                print("The number was: %d" % self.__number)
                return
            
    

def main():
    return Game()

    
if(__name__ == '__main__'):
    main()