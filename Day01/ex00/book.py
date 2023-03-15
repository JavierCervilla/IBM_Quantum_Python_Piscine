#!/usr/bin/env python3

from utils import colors
from recipe import Recipe
from datetime import datetime

class Book:
    
    def __init__(self, name: str):
        self.name: str = (lambda: len(name) > 0 and str(name) or None)()
        self.creation_date: datetime = datetime.now()
        self.last_update: datetime = self.creation_date
        self.recipes_list = {
            "entrante": [],
            "comida": [],
            "postre": [],
        }
        pass
    
    def add_recipe(self, recipe: Recipe) -> Recipe:
        """Add a recipe to the book and update last_update

        Args:
            recipe (Recipe): _description_

        Returns:
            Recipe: _description_
        """
        if not type(recipe) is Recipe:
            return None
        self.recipes_list[recipe.recipe_type()].append(recipe)
        self.last_update = datetime.now()
        return recipe
    
    def get_recipe_by_name(self, name: str) -> Recipe:
        """get a recipe by name

        Args:
            name (str): _description_

        Returns:
            Recipe: _description_
        """
        for type in self.recipes_list:
            for recipe in type:
                if (recipe.name().lower() == name):
                    return recipe
        return None
    
    def get_recipes_by_types(self, recipe_type: str) -> list:
        """get all recipes for a given recipe_type

        Args:
            recipe_type (str): _description_

        Returns:
            list: _description_
        """
        return list(self.recipes_list[recipe_type]) or None
    
    
    def __str__(self) -> str:
        """get the string to print with the recipe info"""
        headers = "Name: {orange}{name}{reset}\nCreation: {green}{creation_date}{reset}\nLast update: {green}{last_update}{reset}\n".format(
            green=colors["green"],
            orange=colors["orange"],
            reset=colors["reset"],
            name = self.name,
            creation_date = self.creation_date.strftime("%d/%m/%Y %H:%M:%S"),
            last_update = self.last_update.strftime("%d/%m/%Y %H:%M:%S"),
        )
        recipes_list = ""
        for key in self.recipes_list:
            recipes_list += "{color}\n{key}S:\n{reset}".format(key=key.upper(), color=colors["orange"], reset=colors["reset"])
            recipes_list += "\n".join(map(lambda recipe: str(recipe), self.recipes_list[key]))
        
        return headers + recipes_list
        
        
    def print(self):
        """Print the book
        """
        print(self.__str__())