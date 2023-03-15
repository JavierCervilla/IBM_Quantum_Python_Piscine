# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javier <javier@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 13:38:34 by javier            #+#    #+#              #
#    Updated: 2023/03/15 17:57:58 by javier           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import sqrt, cos
from utils import test, colors

# COLUMNA: ([[1., 2., 3.]])
# FILA: ([[1.], [2.], [3.]])

class Vector:
    """This Class Represent a Vector"""
    def __init__(self, values):
        if (len(values) == 0):
            raise ValueError("Invalid vector: empty")
        else:
            cols = len(values)
        for i in range(cols):
            rows = len(values[i])
        self.shape = (cols, rows)
        self.values = list()

        for col in range(cols):
            if (len(values) != cols):
                raise ValueError("Invalid vector: not the same size")
            self.values.append(values[col])
    
    
    def map(self, func):
        (cols, rows) = self.shape
        new_vector = list()
        if (cols == 1):
            for row in range(rows):
                for col in range(cols):
                    new_col = list()
                    new_col.append(func(self.values[col][row]))
                new_vector.append(new_col)
        else:
            for col in range(cols):
                for row in range(rows):
                    new_col = list()
                    new_col.append(func(self.values[col][row]))
                new_vector.append(new_col)
        return Vector(new_vector)
    
    def __add__(self, n:float):
        sum = lambda a: n + a
        return self.map(sum)

    def sum(self):
        (cols, rows) = self.shape
        new_vector = list()
        sum = 0.
        if (cols == 1):
            for row in range(rows):
                for col in range(cols):
                    sum += self.values[col][row]
        else:
            for col in range(cols):
                for row in range(rows):
                    sum += self.values[col][row]
        return sum

    #def __sub__(self, p2):
    #    pass

    def __mul__(self, n: float):
        """"Performs a scalar multiplication of a vector by a number n"""
        mul = lambda a: n * a 
        return self.map(mul)

    def __rmul__(self, n: float):
        return self.__mul__(n)

    def abs(self):
        suma = 0
        def squares(a):
            return (a ** 2)
        sq = self.map(lambda a: squares(a))
        return sq.sum()


    def __truediv__(self, n: float):
        try:
            if (n == 0):
                raise ValueError("ZeroDivisionError: division by zero.")
            div = lambda a: a * n
            return self.map(div)
        except Exception as err:
            print("Error: {}".format(err))

    def __rtruediv__(self, n: float):
        return self.__truediv__(n)
            
    
    
    def __str__(self):
        return "Vector({values})".format(values=self.values)
        
if __name__ == "__main__":
    
    def valid_vector_with_all_valid_op():
        n = 2.
        v = Vector([[1., 2., 3.]])
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
        """
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
        """
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
    
    test (
        name="{blue}This is a valid vector with all valid operations.\n{reset}".format(
            blue=colors["blue"], reset=colors["reset"]
        ),
        test=lambda: valid_vector_with_all_valid_op(),
        error="{red}❌ Error: THIS SHOULD NOT BE VISIBLE. IF YOU SHOW ME, YOUR CODE IS BROKEN\n{reset}".format(
            red=colors["red"], reset=colors["reset"]
        ),
        success="{green}✅ TEST PASSED: {orange}This is a valid vector with all valid operations.\n{reset}".format(
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