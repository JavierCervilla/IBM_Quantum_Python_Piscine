#!/usr/bin/env python3

from vector import Vector
from utils import test, colors

def test_all_valid_constructors():
    print("{yellow}Constructor Tamaño:\n\t{purple}Vector(3):\n\t{orange}{v}{reset}".format(
        yellow=colors["yellow"],
        purple=colors["purple"],
        orange=colors["orange"],
        reset=colors["reset"],
        v = str(Vector(3)),
    ))
    print("{yellow}Constructor Vector((3)):\n\t{purple}Vector(3):\n\t{orange}{v}{reset}".format(
        yellow=colors["yellow"],
        purple=colors["purple"],
        orange=colors["orange"],
        reset=colors["reset"],
        v = str(Vector((3))),
    ))
    print("{yellow}Constructor Vector((3,7)):\n\t{purple}Vector(3):\n\t{orange}{v}{reset}".format(
        yellow=colors["yellow"],
        purple=colors["purple"],
        orange=colors["orange"],
        reset=colors["reset"],
        v = str(Vector((3, 7))),
    ))
    print("{yellow}Constructor Vector((1, 10, 2)):\n\t{purple}Vector(3):\n\t{orange}{v}{reset}".format(
        yellow=colors["yellow"],
        purple=colors["purple"],
        orange=colors["orange"],
        reset=colors["reset"],
        v = str(Vector((1, 10, 2))),
    ))
    print("{yellow}Constructor Vector((10, -11, -2)):\n\t{purple}Vector(3):\n\t{orange}{v}{reset}".format(
        yellow=colors["yellow"],
        purple=colors["purple"],
        orange=colors["orange"],
        reset=colors["reset"],
        v = str(Vector((10, -11, -2))),
    ))
    print("{yellow}Constructor Vector((10, -11, -2)):\n\t{purple}Vector(3):\n\t{orange}{v}{reset}".format(
        yellow=colors["yellow"],
        purple=colors["purple"],
        orange=colors["orange"],
        reset=colors["reset"],
        v = str(Vector([[10, -11, -2]])),
    ))

def test_vector_class():
    def valid_vector_tested_with_all_valid_op(v: Vector):
        n = 2
        print("[✅ VALID_OP] SUMA:\n--| {orange}{vector}{blue} + {orange}{num}{reset} = {green}{result}{reset} |--".format(
                vector=str(v),
                num=n,
                result=str(v + n),
                orange=colors["orange"],
                reset=colors["reset"],
                green=colors["green"],
                blue=colors["blue"],
            )
        )
        
        print("[✅ VALID_OP] MULTIPLICACION_L:\n--| {orange}{vector}{blue} * {orange}{num}{reset} = {green}{result}{reset} |--".format(
            vector=str(v),
            num=n,
            result=str(v * n),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[✅ VALID_OP] MULTIPLICACION_R\n--| {orange}{num}{blue} * {orange}{vector}{reset} = {green}{result}{reset} |--".format(
            vector=str(v),
            num=n,
            result=str(n * v),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[✅ VALID_OP] DIVISION_L\n--| {orange}{vector}{blue} / {orange}{num}{reset} = {green}{result}{reset} |--".format(
            vector=str(v),
            num=n,
            result=str(v / n),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        # ESTA FUNCION DA ERROR YA QUE NO SE PUEDE DIVIDIR UN NUMERO ENTRE UN VECTOR
        print("[❌ INVALID_OP] DIVISION_R\n--| {orange}{num}{blue} / {orange}{vector}{reset} = {green}{result}{reset} |--".format(
            vector=str(v),
            num=n,
            result=str(n / v),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[❌ INVALID_OP] DIVISION ZERO:\n--| {orange}{vector}{blue} / {orange}{num}{reset} = {green}{result}{reset} |--".format(
            vector=str(v),
            num=0,
            result=str(v / 0),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[✅ VALID_OP] MODULE:\n--| {orange}modulo de {vector}{reset} = {green}{result}{reset} |--".format(
            vector=str(v),
            num=0,
            result=v.abs(),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        return v
    
    print("{color}{text:🀫^110}{reset}".format(
        text="| START OF UNITARY TESTS OF CLASS VECTOR IN vector.py |",
        color=colors["purple"],
        reset=colors["reset"]
    ))

    test (
        name="{blue}This is a valid ROW VECTOR with ALL VALID AND INVALID OPs.\n{reset}".format(
            blue=colors["blue"], reset=colors["reset"]
        ),
        test=lambda: valid_vector_tested_with_all_valid_op(v=Vector([[1., 2., 3.]])),
        error="{red}❌ Error: THIS SHOULD NOT BE VISIBLE. IF YOU SHOW ME, YOUR CODE IS BROKEN\n{reset}".format(
            red=colors["red"], reset=colors["reset"]
        ),
        success="{green}✅ TEST PASSED: {orange}This is a valid vector with all valid and invalid operations.\n{reset}".format(
            green=colors["green"], reset=colors["reset"], orange=colors["orange"]
        )
    )

    test (
        name="{blue}This is a valid COLUMN VECTOR with ALL VALID AND INVALID OPs.\n{reset}".format(
            blue=colors["blue"], reset=colors["reset"]
        ),
        test=lambda: valid_vector_tested_with_all_valid_op(v=Vector([[1.], [2.], [3.]])),
        error="{red}❌ Error: THIS SHOULD NOT BE VISIBLE. IF YOU SHOW ME, YOUR CODE IS BROKEN\n{reset}".format(
            red=colors["red"], reset=colors["reset"]
        ),
        success="{green}✅ TEST PASSED: {orange}This is a valid vector with all valid and invalid operations.\n{reset}".format(
            green=colors["green"], reset=colors["reset"], orange=colors["orange"]
        )
    )

    test (
        name="{blue}This is a valid COLUMN VECTOR with ALL VALID AND INVALID OPs.\n{reset}".format(
            blue=colors["blue"], reset=colors["reset"]
        ),
        test=lambda: test_all_valid_constructors(),
        error="{red}❌ Error: THIS SHOULD NOT BE VISIBLE. IF YOU SHOW ME, YOUR CODE IS BROKEN\n{reset}".format(
            red=colors["red"], reset=colors["reset"]
        ),
        success="{green}✅ TEST PASSED: {orange}This is a valid vector with all valid and invalid operations.\n{reset}".format(
            green=colors["green"], reset=colors["reset"], orange=colors["orange"]
        )
    )
    
    print("{color}{text:🀫^110}{reset}".format(
        text="| END OF UNITARY TESTS OF CLASS VECTOR IN vector.py |",
        color=colors["purple"],
        reset=colors["reset"]
    ))

if __name__ == "__main__":
    test_vector_class()