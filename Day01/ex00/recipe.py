# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javier <javier@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 15:19:59 by javier            #+#    #+#              #
#    Updated: 2023/03/15 02:22:29 by javier           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import colors


RECIPE_TYPES = ["entrante", "comida", "postre"]

class Recipe:
    """Class to represent a recipe"""
    
    def __checker__(self, **functions):
        for key in functions:
            if functions[key]() == None:
                raise ValueError("Invalid value for {}".format(key))
                
    
    def __init__(self, **kwargs):
        name = lambda: "name" in kwargs and 100 > len(str(kwargs["name"])) > 0 and str(kwargs["name"]) or None
        description = lambda: str(kwargs["description"])  if "description" in kwargs else ""
        cooking_level = lambda: 0 < int(kwargs["cooking_lvl"]) <= 5 and int(kwargs["cooking_lvl"]) or None
        cooking_time = lambda: int(kwargs["cooking_time"]) and int(kwargs["cooking_time"]) >= 0 and int(kwargs["cooking_time"]) or None
        ingredients = lambda: "ingredients" in kwargs and len(kwargs["ingredients"]) > 0 and list(filter(lambda s: len(s) > 0, list(kwargs["ingredients"])))  or None
        recipe_type = lambda: str(kwargs["recipe_type"]) and str(kwargs["recipe_type"]).lower() in RECIPE_TYPES and str(kwargs["recipe_type"]) or None
        self.__checker__(name=name, description=description, cooking_level=cooking_level, cooking_time=cooking_time, ingredients=ingredients, recipe_type=recipe_type)

        self.dict = {
            "_id": int(kwargs["_id"]),
            "name": name(),
            "description": len(str(description())) <= 500 and description() ,
            "cooking_lvl": cooking_level(),
            "cooking_time": int(kwargs["cooking_time"]) and int(kwargs["cooking_time"]) >= 0 and int(kwargs["cooking_time"]) or 1,
            "ingredients": ingredients(),
            "recipe_type": recipe_type()
        }
    
    def _id(self):
        return int(self.dict.get("_id"))
        
    def name(self):
        return str(self.dict.get("name"))
    
    def description(self):
        if ("description" not in self.dict):
            return None
        return str(self.dict.get("description"))

    def cooking_lvl(self):
        return int(self.dict.get("cooking_lvl"))

    def cooking_time(self):
        return int(self.dict.get("cooking_time"))

    def ingredients(self):
        return list(self.dict.get("ingredients"))
    
    def recipe_type(self):
        return str(self.dict.get("recipe_type"))

    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        if (self.dict == None):
            return str(self.dict)
        return "[{orange}{_id}{reset}] Name: {green}{name}{reset}\nDescription: {green}{description}{reset}\n - lvl: {green}{cooking_lvl}{reset}\n - time: {green}{cooking_time}{reset}\n - type: {green}{recipe_type}{reset}\n - ingredientes: {green}{ingredients}{reset}\n".format(
            red=colors["red"],
            orange=colors["orange"],
            green=colors["green"],
            reset=colors["reset"],
            _id=self._id(),
            name=self.name(),
            description=self.description() or "",
            cooking_lvl=self.cooking_lvl(),
            cooking_time=self.cooking_time(),
            recipe_type=self.recipe_type(),
            ingredients=self.ingredients(),
        )

    def print(self):
        print(self.__str__())