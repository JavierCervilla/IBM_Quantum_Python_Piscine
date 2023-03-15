#!/usr/bin/env python3
from utils import colors, test
from recipe import Recipe

def recipe_tests():
    
    # FULL VALID CLASS:
    test(
        name="It SHOULD create a FULL CLASS WITH DESCRIPTION and print it.",
        test=lambda: Recipe(
            _id=1,
            name="Bocata de Calamares",
            cooking_lvl=3,
            cooking_time=15,
            ingredients=["Pan", "Calamares", "Mahonesa"],
            description="Rico Bocata para disfrutar paseando por el centro de Madrid.",
            recipe_type="entrante",
        ),
        error=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN." + colors["reset"],
        success=colors["green"] + "✅ TEST PASSED: The RECIPE is VALID and FULL ." + colors["reset"]
    ) 
    
    # VALID CLASS W/O DESCRIPTION:
    test(
        name=colors["yellow"] + "It SHOULD create a CLASS W/O DESCRIPTION and print anyways" + colors["reset"],
        test=lambda: Recipe(
            _id=2,
            name="Bocata de Calamares",
            cooking_lvl=3,
            cooking_time=15,
            ingredients=["Pan", "Calamares", "Mahonesa"],
            recipe_type="entrante",
        ),
        success=colors["green"] + "✅ TEST PASSED: The recipe is VALID W/O DESCRIPTION." + colors["reset"],
        error=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN."
    ) 
    
    # INVALID CLASS W/O NAME: ERROR
    test(
        name=colors["yellow"] + "It Should NOT create a VALID CLASS recipe without name." + colors["reset"],
        test=lambda: Recipe(
            _id=3,
            cooking_lvl=3,
            cooking_time=15,
            ingredients=["Pan", "Calamares", "Mahonesa"],
            description="Rico Bocata para disfrutar paseando por el centro de Madrid.",
            recipe_type="entrante",
        ),
        error=colors["green"] + "✅ TEST PASSED: The recipe is not valid, it throws a error correctly, and no instance returned." + colors["reset"],
        success=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN.",
    )
    # INVALID CLASS W/O INGREDIENTS ERROR
    test(
        name=colors["yellow"] + "It Should NOT create a VALID CLASS because W/O INGREDIENTS." + colors["reset"],
        test=lambda: Recipe(
            _id=4,
            name="Bocata de Calamares",
            cooking_lvl=3,
            cooking_time=15,
            description="Rico Bocata para disfrutar paseando por el centro de Madrid.",
            recipe_type="entrante",
        ),
        error=colors["green"] + "✅ TEST PASSED: The recipe is not valid, it throws a error correctly, and no instance returned." + colors["reset"],
        success=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN.",
    )
    # INVALID CLASS COOKING LVL ERROR
    test(
        name=colors["yellow"] + "It Should NOT create a VALID CLASS because COOOKING_LVL is OUT OF RANGE." + colors["reset"],
        test=lambda: Recipe(
            _id=5,
            name="Bocata de Calamares",
            cooking_lvl=6,
            cooking_time=15,
            ingredients=["Pan", "Calamares", "Mahonesa"],
            description="Rico Bocata para disfrutar paseando por el centro de Madrid.",
            recipe_type="entrante",
        ),
        error=colors["green"] + "✅ TEST PASSED: The recipe is not valid, it throws a error correctly, and no instance returned." + colors["reset"],
        success=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN.",
    )
    # INVALID CLASS NO INGREDIENTS  ERROR
    test(
        name=colors["yellow"] + "It Should NOT create a VALID CLASS because INGREDIENTS are EMPTY." + colors["reset"],
        test=lambda: Recipe(
            _id=6,
            name="Bocata de Calamares",
            cooking_lvl=3,
            cooking_time=15,
            ingredients=[],
            description="Rico Bocata para disfrutar paseando por el centro de Madrid.",
            recipe_type="entrante",
        ),
        error=colors["green"] + "✅ TEST PASSED: The recipe is not valid, it throws a error correctly, and no instance returned." + colors["reset"],
        success=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN.",
    )
    # INVALID CLASS INGREDIENTS EMPTY STRING  ERROR
    test(
        name=colors["yellow"] + "It Should create a VALID CLASS REMOVING ALL EMPTY INGREDIENTS STRINGS." + colors["reset"],
        test=lambda: Recipe(
            _id=7,
            name="Bocata de Calamares",
            cooking_lvl=3,
            cooking_time=15,
            ingredients=["", "", "calamares"],
            description="Rico Bocata para disfrutar paseando por el centro de Madrid.",
            recipe_type="entrante",
        ),
        success=colors["green"] + "✅ TEST PASSED: The recipe is VALID W/O EMPTY INGREDIENTS STRINGS." + colors["reset"],
        error=colors["red"] + "❌ ERROR: THIS SHOULD NOT BE VISIBLE. IF YOU VIEW ME YOUR CODE IS BROKEN.",
    )
    
    return
    
if(__name__ == '__main__'):
    recipe_tests()