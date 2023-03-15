#!/usr/bin/env python3
from utils import colors, test
from book import Book
from recipe import Recipe



invalid_not_recipe = lambda: None

invalid_recipe = lambda: Recipe(
                _id=1,
                name="Bocata de Calamares",
                cooking_lvl=6,
                cooking_time=15,
                ingredients=["Pan", "Calamares", "Mahonesa"],
                recipe_type="entrante",
            )
valid_entrante_recipe = lambda: Recipe(
                _id=1,
                name="Bocata de Calamares",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["Pan", "Calamares", "Mahonesa"],
                recipe_type="entrante",
            )
valid_postre_recipe = lambda: Recipe(
                _id=1,
                name="Arroz con Leche",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["Arroz", "Leche", "Canela"],
                description="Rico arroz con leche y canela.",
                recipe_type="postre",
            )
valid_comida_recipe = lambda: Recipe(
                _id=1,
                name="Tarta de Calamares",
                cooking_lvl=3,
                cooking_time=15,
                ingredients=["Pan", "Calamares", "Mahonesa"],
                description="Rico Bocata para disfrutar paseando por el centro de Madrid.",
                recipe_type="comida",
            )

def book_tests():
    
    """ # FULL VALID NO RECIPES CLASS:
    test(
        name="It SHOULD create a FULLY FUNCTIONAL CLASS W/O RECIPES and print it.",
        test=lambda: Book(name="My Book"),
        error=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN." + colors["reset"],
        success=colors["green"] + "✅ TEST PASSED: The BOOK is VALID and FULL ." + colors["reset"]
    )
    
    # INVALID NO NAME CLASS:
    test(
        name="It SHOULD NOT CREATE a VALID CLASS W/O NAME.",
        test=lambda: Book(),
        success=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN." + colors["reset"],
        error=colors["green"] + "✅ TEST PASSED: The BOOK W/O NAME is NOT INSTANTIATED." + colors["reset"]
    )
    # FULL VALID WITH RECIPES CLASS:
    test(
        name="It SHOULD create a FULLY FUNCTIONAL CLASS W/O RECIPES and print it.",
        test=lambda: Book(name="My Book"),
        error=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN." + colors["reset"],
        success=colors["green"] + "✅ TEST PASSED: The BOOK is VALID and FULL ." + colors["reset"]
    ) """
    
    def create_a_book_and_add_valid_recipe():
        book = Book(name="My Book")
        book.add_recipe(
            recipe=valid_entrante_recipe()
        )
        book.add_recipe(
            recipe=valid_postre_recipe()
        )
        book.add_recipe(
            recipe=valid_comida_recipe()
        )
        return book
    
    def create_a_book_and_add_invalid_recipe(recipe):
        book = Book(name="My Book")
        book.add_recipe(
            recipe=recipe
        )
        return book
    
    
    # VALID BOOK WITH VALID RECIPE:
    test(
        name="It SHOULD create a FULLY FUNCTIONAL BOOK W/O RECIPES, ADD a RECIPE for each type and print it.",
        test=lambda: create_a_book_and_add_valid_recipe(),
        error=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN." + colors["reset"],
        success=colors["green"] + "✅ TEST PASSED: The BOOK is VALID and FULL of RECIPES." + colors["reset"]
    )
    
    # VALID BOOK WITH INVALID RECIPE of type RECIPE:
    test(
        name="It SHOULD create a FULLY FUNCTIONAL BOOK W/O RECIPES, NOT ADD any RECIPE.",
        test=lambda: create_a_book_and_add_invalid_recipe(invalid_recipe()),
        success=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN." + colors["reset"],
        error=colors["green"] + "✅ TEST PASSED: The BOOK is VALID and RECIPES NOT ADDED." + colors["reset"]
    )
    # VALID BOOK WITH INVALID RECIPE of type NOT RECIPE:
    test(
        name="It SHOULD create a FULLY FUNCTIONAL BOOK W/O RECIPES, NOT ADD any RECIPE.",
        test=lambda: create_a_book_and_add_invalid_recipe(None),
        error=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN." + colors["reset"],
        success=colors["green"] + "✅ TEST PASSED: The BOOK is VALID and RECIPES NOT ADDED." + colors["reset"]
    )
    
    return


    
if(__name__ == '__main__'):
    book_tests()