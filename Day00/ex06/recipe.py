#!/usr/bin/env python3
import sys
cookbook = {}

bocadillo = {
    "ingredients": [
        "jamón",
        "pan",
        "queso",
        "tomate"
    ],
    "meal": "almuerzo",
    "prep_time": 10
}

tarta = {
    "ingredients": [
        "harina",
        "azucar",
        "huevos"
    ],
    "meal": "postre",
    "prep_time": 60
}

ensalada = {
    "ingredients": [
        "aguacate",
        "rúcula",
        "tomates",
        "espinacas"
    ],
    "meal": "almuerzo",
    "prep_time": 15
}

def print_prompt():
    print("Welcome to the Python Cookbook!\nList of available option:\n 1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe\n 4: Print the cookbook\n 5: Quit\n")

def print_recipes():
    for name in cookbook:
        print(name)
        
def print_recipe(name):
    try:
        if (cookbook.get(name) == None):
            raise TypeError
        print("Recipe for {name}:\nIngredients List: {ingredients}\nTo be eaten for {meal}.\nTakes {prep_time} minutes of cooking.\n".format(
            name=name,
            ingredients=cookbook[name]["ingredients"],
            meal=cookbook[name]["meal"],
            prep_time=cookbook[name]["prep_time"]
        ))
    except:
        print("Error: Recipe not found in cookbook\n")

def delete_recipe(name):
    try:
        if (cookbook.get(name) == None):
            raise TypeError
        del cookbook[name]
    except:
        print("Error: Recipe not found in cookbook\n")

def add_recipe():
    name = input("Enter a name:\n")
    ingredients = []
    new_ingredient = input("Enter ingredients:\n")
    while(new_ingredient != ""):
        ingredients.append(new_ingredient)
        new_ingredient = input()
    meal = input("Enter a meal type:\n")
    prep_time = input("Enter a prep time:\n")
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print_recipe(name)

def main():
    cookbook["bocadillo"] = bocadillo
    cookbook["tarta"] = tarta
    cookbook["ensalada"] = ensalada
    print_prompt()
    stdin = input("Please select an option:\n>> ")
    while(stdin != "5"):
        if (stdin == "1"):
            add_recipe()
        elif (stdin == "2"):
            name = input("\nEnter a name:\n")
            delete_recipe(name)
        elif (stdin == "3"):
            name = input("\nEnter a name:\n")
            print_recipe(name)
        elif (stdin == "4"):
            print_recipes()
        else:
            print("Error: Invalid option\n")
        stdin = input("Please select an option:\n")
    print("\nCookbook closed. Goodbye!\n")
    return
    
if(__name__ == '__main__'):
    main()