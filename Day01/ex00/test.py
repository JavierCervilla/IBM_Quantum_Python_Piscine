#!/usr/bin/env python3
from recipe_test import recipe_tests
from book_test import book_tests
from utils import colors

def main():
    """ # RECIPES TESTS:
    print("{color}{text:🀫^110}{reset}".format(
        text="| START OF UNITARY TESTS OF CLASS RECIPE IN recipe.py |",
        color=colors["purple"],
        reset=colors["reset"]
    ))
    recipe_tests()
    print("{color}{text:🀫^110}{reset}".format(
        text="| END OF UNITARY TESTS OF CLASS RECIPE IN recipe.py |",
        color=colors["purple"],
        reset=colors["reset"]
    )) """
    # BOOK TESTS:
    print("{color}{text:🀫^110}{reset}".format(
        text="| START OF UNITARY TESTS OF CLASS BOOK IN book.py |",
        color=colors["purple"],
        reset=colors["reset"]
    ))
    book_tests()
    print("{color}{text:🀫^110}{reset}".format(
        text="| ENF OF UNITARY TESTS OF CLASS BOOK IN book.py |",
        color=colors["purple"],
        reset=colors["reset"]
    ))
    return
    
if(__name__ == '__main__'):
    main()
