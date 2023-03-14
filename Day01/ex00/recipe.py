# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javier <javier@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 15:19:59 by javier            #+#    #+#              #
#    Updated: 2023/03/14 21:57:53 by javier           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

RECIPE_TYPES = ["entrante", "comida", "postre"]

class Recipe:
    def __init__(self, **kwargs):
        description = ""
        if "description" in kwargs:
            description = str(kwargs["description"])
        
        if (0 < int(kwargs["cooking_lvl"]) <= 5):
            cooking_level = int(kwargs["cooking_lvl"])
        else:
            raise ValueError("Cooking level must be between 1 and 5")
        if "ingredients" in kwargs and len(list(kwargs["ingredients"])) > 0:
            ingredients = list(kwargs["ingredients"])
        else:
            raise ValueError("Ingredients must be a list with at least one element")
        
        if "name" in kwargs and 100 > len(str(kwargs["name"])) > 0:
            name = str(kwargs["name"])
        else:
            raise ValueError("Name must be a string with at least one character and less than 100")
        
        if str(kwargs["recipe_type"]) and str(kwargs["recipe_type"]).lower() in RECIPE_TYPES:
            recipe_type = kwargs["recipe_type"].lower()
        self.dict = {
            "_id": int(kwargs["_id"]),
            "name": str(kwargs["name"]) and 0 < len(str(kwargs["name"])) <= 100  and str(kwargs["name"]) ,
            "description": len(str(description)) <= 500 and description ,
            "cooking_lvl": cooking_level,
            "cooking_time": int(kwargs["cooking_time"]) and int(kwargs["cooking_time"]) >= 0 and int(kwargs["cooking_time"]) or 1,
            "ingredients": ingredients,
            "recipe_type": recipe_type
        }

    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        if (self.dict == None):
            return str(self.dict)
        return "[{_id}] {name:<100}\n{description} - lvl: {cooking_lvl:^3}\n - time: {cooking_time:^6}\n - type: {recipe_type}\n - ingredientes:\n   {ingredients}\n".format(
            _id=self.dict.get("_id"),
            name=self.dict.get("name"),
            description=str(self.dict.get("description")) + "\n" or "",
            cooking_lvl=self.dict.get("cooking_lvl"),
            cooking_time=self.dict.get("cooking_time"),
            recipe_type=self.dict.get("recipe_type"),
            ingredients=self.dict.get("ingredients"),
        )

    def print(self):
        print(self.__str__())