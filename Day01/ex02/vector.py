# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javier <javier@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 13:38:34 by javier            #+#    #+#              #
#    Updated: 2023/03/16 20:43:21 by javier           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import sqrt, cos
from utils import colors

# COLUMNA: ([[1., 2., 3.]])
# FILA: ([[1.], [2.], [3.]])

# [[0.]*sample[0]] for i in range(sample[1])

class Vector:
    """This Class Represent a Vector"""

    def __init__(self, values):
        if (isinstance(values, int)):
            return self.__init_with_size__(size=values)
        if (isinstance(values, tuple)):
            return self.__init_with_range__(_range=values)
        if (isinstance(values, list)):
            return self.__init_with_list__(values=values)
        else:
            raise ValueError("Constructor of type: {} not exists.".format(type(values)))

    def __init_with_list__(self, values: list):
        if (len(values) == 0):
            raise ValueError("Invalid vector list: empty")
        else:
            rows = len(values)
        cols = 0
        for i in range(rows):
            cols = len(values[i]) if type(values[i]) == list else 1
        self.shape = (rows, cols)
        self.values = list()
        for row in range(rows):
            if (len(values) != rows):
                raise ValueError("Invalid vector: not all rows have the same size")
            self.values.append(values[row])

    def __init_with_size__(self, size: int):
        if (size <= 0):
            raise ValueError("Invalid range: Range values out of range. Must be 1 or 2 values")
        self.values = [[float(i)] for i in range(size)]
        self.shape = (len(self.values), 1)

    def __init_with_range__(self, _range: range):
        if (len(_range) == 0 or len(_range) > 3):
            raise ValueError("Invalid range: Range values out of range.")
        if (len(_range) >= 2 and (_range[0] >= _range[1] and len(_range) == 2)):
            raise ValueError("Invalid range: start must be less than end")
        if (len(_range) == 1):
            self.values = [[float(i)] for i in range(_range[0])]
        elif (len(_range) == 2):
            self.values = [[float(i)] for i in range(_range[0], _range[1])]
        elif (len(_range) == 3):
            if (_range[2] == 0):
                raise ValueError("Invalid range: step must be non-zero and smaller than the start and end values")
            if (_range[2] > 0 and _range[0] >= _range[1]):
                raise ValueError("Invalid range: start must be less than end when step is positive")
            if (_range[2] < 0 and _range[0] <= _range[1]):
                raise ValueError("Invalid range: start must be greater than end when step is negative")
            self.values = [[float(i)] for i in range(_range[0], _range[1], _range[2])]
        self.shape = (len(self.values), 1)

    def iter(self, func):
        """
            func: lambda row, col: value
            Applies a function to all elements of the vector and returns a new vector containing the results
        """
        (rows, cols) = self.shape
        new_vector = list()
        for row in range(rows):
            for col in range(cols):
                new_col = list()
                if (rows == 1):
                    new_col = func(row, col)
                else:
                    new_col.append(func(row, col))
                new_vector.append(new_col)
        return Vector(new_vector)

    def sum(self):
        """ Returns the sum of all elements of the vector """
        (rows, cols) = self.shape
        suma = 0.

        for row in range(rows):
            for col in range(cols):
                if (rows == 1):
                    suma += self.values[row][col]
                elif (cols == 1):
                    suma +=  sum(self.values[row]) if isinstance(self.values[row], list) else self.values[row]
        return suma

    """ def __add__(self, v2):
        #Performs an addition of a vector by a vector n in all elements of the vector
        v2 = v2 if isinstance(v2, Vector) and v2.shape == self.shape else None
    """
    
    def __add__(self, n:float):
        """ Performs an addition of a vector by a number n in all elements of the vector """
        print("LLEGO A ADD")
        sum = lambda row,col: n + self.values[row][col]
        return self.iter(sum)
    
    def __radd__(self, n:float):
        """ Performs an addition of a vector by a number n in all elements of the vector for the right """
        return self.__add__(n)

    def __sub__(self, n: float):
        """ Performs a substraction of a vector by a number n in all elements of the vector """
        return self.__add__(-n)

    def __mul__(self, n: float):
        """" Performs a multiplication of a vector by a number n in all elements of the vector"""
        mul = lambda row, col: n * self.values[row][col]
        return self.iter(mul)
        

    def __rmul__(self, n: float):
        """" Performs a multiplication of a vector by a number n in all elements of the vector for the right """
        return self.__mul__(n)

    def abs(self) -> float:
        """" Returns a module for a vector """
        def squares(a):
            return (a ** 2)
        sq = self.iter(lambda row, col: squares(self.values[row][col]))
        return sq.sum() ** 0.5


    def __truediv__(self, n: float):
        """" Performs a multiplication of a vector by a number n in all elements of the vector"""
        try:
            if (n == 0):
                raise ValueError("ZeroDivisionError: division by zero.")
            return self.iter(lambda row, col: self.values[row][col] / n)
        except Exception as error:
            self.__error__(error=error)

    def __error__(self, error):
        print("{red}Error: {error}{reset}".format(
            error=error,
            red=colors["red"],
            reset=colors["reset"]
        ))

    def __rtruediv__(self, n: float):
        """" Performs a multiplication of a vector by a number n in all elements of the vector"""
        try:
            raise Exception("NotImplementedError: Division of a scalar by a Vector is not defined here.")
        except Exception as error:
            self.__error__(error=error)
    
    def dot(self, v2):
        v2 = v2 if isinstance(v2, Vector) and v2.shape == self.shape else None
        prod_esc = lambda row, col: float(self.values[row][col]) * float(v2.values[row][col])
        return self.iter(prod_esc).sum()
    
    def T(self):
        """ Transpose a vector """
        (rows, cols) = self.shape
        new_vector = list()
        for row in range(rows):
            for col in range(cols):
                if (rows == 1):
                    new_vector.append([self.values[row][col]])
                else:
                    new_vector.append(self.values[row][col])
        return Vector(new_vector if rows == 1 else [new_vector])
                    

    def __str__(self):
        (cols, rows) = self.shape
        return "Vector({values}) <c={cols}|r={rows}>".format(
            values=self.values,
            rows=rows,
            cols=cols
        )




######################################################################
##
## 🆘 DEBUG AREA
##
######################################################################
##
##
##        v1 = Vector([[1., 2., 3.]])
##        print("Vector([[1., 2., 3.]])", str(v1))
##        n = 2
##        print("{} + {} = {}".format(str(v1), n, str(v1 + n)))
##        
##        v1 = Vector([[1., 2., 3.]])
##        print("Vector([[1., 2., 3.]])", str(v1))
##        v1 = Vector(5)
##        print("Vector(5)", str(v1))
##        v1 = Vector((10,16))
##        print("Vector((10,16))", str(v1))
##        v1 = Vector([[1., 2., 3.]])
##        print("{} * {} = {}".format(n, str(v1), str(n * v1)))
##        print("{} / {} = {}".format(str(v1), n, str(v1 / n)))
##        print("{} / {} = {}".format(str(v1), 0, str(v1 / 0)))
##        print("{} X {} = {}".format(str(v1), str(v1), str(v1.dot(v1))))
##        print("ABS(Module): {}".format(v1.abs()))
##        
##        v1 = Vector([[1.], [3.],[3.]])
##        print("Vector([[1.], [2.],[3.]])", str(v1))
##        
##        print("{} * {} = {}".format(str(v1), n, str(v1 * n)))
##        print("{} * {} = {}".format(n, str(v1), str(n * v1)))
##        print("{} / {} = {}".format(str(v1), n, str(v1 / n)))
##        print("{} / {} = {}".format(str(v1), 0, str(v1 / 0)))
##        print("{} X {} = {}".format(str(v1), str(v1), str(v1.dot(v1))))
##        print("ABS(Module): {}".format(v1.abs()))
##        v1 = Vector([[1., 2., 3.]])
##        print("TO TRASPOSE:\n\t{}".format(str(v1)))
##        print("Traspose: {}".format(str(v1.T())))
##        
##        v1 = Vector([[1.], [2.], [3.]])
##        print("TO TRASPOSE:\n\t{}".format(str(v1)))
##        print("Traspose: {}".format(str(v1.T())))
##        
##
##########################################################################