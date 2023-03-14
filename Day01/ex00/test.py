#!/usr/bin/env python3

from recipe import Recipe

def main():
    recipe = Recipe(
        _id=1,
        name="Bocata de Calamares",
        description="Rico Bocata para disfrutar paseando por el centro de Madrid.",
        cooking_lvl=6,
        cooking_time=15,
        recipe_type="entrante",
        ingredients=["Pan", "Calamares", "Mahonesa"],
    )
    recipe.print()
    return
    
if(__name__ == '__main__'):
    main()
