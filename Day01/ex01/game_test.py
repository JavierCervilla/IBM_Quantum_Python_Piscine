#!/usr/bin/env python3
from utils import colors, test
from game import Stark


def create_valid_stark_with_name(first_name="Arya", is_alive=True):
    arya = Stark(first_name=first_name, is_alive=is_alive)
    print(colors["white"])
    print("{blue}__dict__ : {yellow}{dict}{reset}\n{blue}str(instance) : {yellow}{s}{reset}\n{blue}{blue}name : {yellow}{name}{reset}\n{blue}house_words : {yellow}{msg}{reset}".format(
        dict=arya.__dict__,
        blue=colors["cyan"],
        reset=colors["reset"],
        yellow=colors["yellow"],
        s=str(arya),
        name=arya.first_name,
        msg=arya.house_words
    ))
    
    print(colors["reset"])
    return arya

def create_valid_stark_without_name():
    noname = Stark(is_alive=True)
    
    print("{blue}__dict__ : {yellow}{dict}{reset}\n{blue}str(instance) : {yellow}{s}{reset}\n{blue}{blue}name : {yellow}{name}{reset}\n{blue}house_words : {yellow}{msg}{reset}".format(
        dict=noname.__dict__,
        blue=colors["cyan"],
        reset=colors["reset"],
        yellow=colors["yellow"],
        s=str(noname),
        name=noname.first_name,
        msg=noname.house_words
    ))
    
    return noname

def game_tests():
    
    # FULL VALID CLASS WITH NAME:
    test(
        name="It SHOULD create a FULL CLASS WITH && print __dict__ && print house_words && print alive.",
        test=lambda: create_valid_stark_with_name(first_name="Arya", is_alive=True),
        error="{red}❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN.{reset}".format(red=colors["red"], reset=colors["reset"]),
        success="{green}✅ TEST PASSED: The STARK is VALID and FULL.{reset}".format(green=colors["green"], reset=colors["reset"]),
    )
    
    test(
        name="It SHOULD create a FULL CLASS WITH && print __dict__ && print house_words && print alive.",
        test=lambda: create_valid_stark_without_name(),
        error="{red}❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN.{reset}".format(red=colors["red"], reset=colors["reset"]),
        success="{green}✅ TEST PASSED: The STARK is VALID and HAS NOT NAME.{reset}".format(green=colors["green"], reset=colors["reset"]),
    )
    
    return
    
if(__name__ == '__main__'):
    game_tests()