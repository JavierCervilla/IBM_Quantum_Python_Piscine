#!/usr/bin/env python3

from vector import Vector
from utils import test, colors

def test_vector_class():
    def valid_vector_tested_with_all_valid_op(v: Vector):
        n = 2
        print("[{orange}{vector}{blue} + {orange}{num}{reset} = {green}{result}{reset}]".format(
                vector=str(v),
                num=n,
                result=str(v + n),
                orange=colors["orange"],
                reset=colors["reset"],
                green=colors["green"],
                blue=colors["blue"],
            )
        )
        print("[{orange}{vector}{blue} * {orange}{num}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=n,
            result=str(v * n),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[{orange}{num}{blue} * {orange}{vector}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=n,
            result=str(n * v),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[{orange}{vector}{blue} / {orange}{num}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=n,
            result=str(v / n),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        # ESTA FUNCION DA ERROR YA QUE NO SE PUEDE DIVIDIR UN NUMERO ENTRE UN VECTOR
        print("[{orange}{num}{blue} / {orange}{vector}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=n,
            result=str(n / v),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[{orange}{vector}{blue} / {orange}{num}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=0,
            result=str(v / 0),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[{orange}modulo de {vector}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=0,
            result=v.abs(),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        return v
    
    def valid_vector_tested_with_invalid_op__rtruediv__(v: Vector):
        n = 2.
        print("[{orange}{vector}{blue} + {orange}{num}{reset} = {green}{result}{reset}]".format(
                vector=str(v),
                num=n,
                result=str(v + n),
                orange=colors["orange"],
                reset=colors["reset"],
                green=colors["green"],
                blue=colors["blue"],
            )
        )
        print("[{orange}{vector}{blue} * {orange}{num}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=n,
            result=str(v * n),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[{orange}{num}{blue} * {orange}{vector}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=n,
            result=str(n * v),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[{orange}{vector}{blue} / {orange}{num}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=n,
            result=str(v / n),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        # ESTA FUNCION DA ERROR YA QUE NO SE PUEDE DIVIDIR UN NUMERO ENTRE UN VECTOR
        print("[{orange}{num}{blue} / {orange}{vector}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=n,
            result=str(n / v),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[{orange}{vector}{blue} / {orange}{num}{reset} = {green}{result}{reset}]".format(
            vector=str(v),
            num=0,
            result=str(v / 0),
            orange=colors["orange"],
            reset=colors["reset"],
            green=colors["green"],
            blue=colors["blue"],
        ))
        print("[{orange}modulo de {vector}{reset} = {green}{result}{reset}]".format(
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
        test=lambda: valid_vector_tested_with_all_valid_op(v=[[1.], [2.], [3.]]),
        error="{red}❌ Error: THIS SHOULD NOT BE VISIBLE. IF YOU SHOW ME, YOUR CODE IS BROKEN\n{reset}".format(
            red=colors["red"], reset=colors["reset"]
        ),
        success="{green}✅ TEST PASSED: {orange}This is a valid vector with all valid and invalid operations.\n{reset}".format(
            green=colors["green"], reset=colors["reset"], orange=colors["orange"]
        )
    )
    """ v2 = Vector([[1.], [2.], [3.]])
    print("{} * {} = {}".format(str(v2), n, str(v2 * n)))
    print("{} * {} = {}".format(n, str(v2), str(n * v2)))
    print("{} / {} = {}".format(str(v2), n, str(v2 / n)))
    #print("{} / {} = {}".format(n, str(v2, str(n / v2))))
    print("{} / {} = {}".format(str(v2), 0, str(v2 / 0)))

    print(v2.abs())

    v3 = Vector([[5.0, 1.0, 2.0, 3.0]])

    print("{} * {} = {}".format(str(v3), n, str(v3 * n)))
    print("{} * {} = {}".format(n, str(v3), str(n * v3)))
    print("{} / {} = {}".format(str(v3), n, str(v3 / n)))
    #print("{} / {} = {}".format(n, str(v3, str(n / v3))))
    print("{} / {} = {}".format(str(v3), 0, str(v3 / 0)))

    print(v3.abs()) """

    """ v2 = Vector([[1.], [2.], [3.]])
    print(str(v2))
    m1 = Vector([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
    print(str(m1)) """
    
    
    print("{color}{text:🀫^110}{reset}".format(
        text="| END OF UNITARY TESTS OF CLASS VECTOR IN vector.py |",
        color=colors["purple"],
        reset=colors["reset"]
    ))

if __name__ == "__main__":
    test_vector_class()