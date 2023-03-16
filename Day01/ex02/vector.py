# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javier <javier@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 13:38:34 by javier            #+#    #+#              #
#    Updated: 2023/03/16 01:18:00 by javier           ###   ########.fr        #
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
        if (len(values) == 0):
            raise ValueError("Invalid vector: empty")
        else:
            cols = len(values)
        rows = 0
        for i in range(cols):
            rows = len(values[i]) if type(values[i]) == list else rows + 1
        self.shape = (cols, rows)
        self.values = list()
        for col in range(cols):
            if (len(values) != cols):
                raise ValueError("Invalid vector: not all rows have the same size")
            self.values.append(values[col])

    def iter(self, func):
        """
            func: lambda row, col: value
            Applies a function to all elements of the vector and returns a new vector containing the results
        """
        (cols, rows) = self.shape
        new_vector = list()
        if (cols == 1):
            for col in range(cols):
                new_row = list()
                for row in range(rows):
                    new_col = func(row, col)
                    new_row.append(new_col)
                new_vector.append(new_row)
        else:
            for col in range(cols):
                for row in range(rows):
                    new_col = list()
                    new_col.append(func(row, col))
                new_vector.append(new_col)
        return Vector(new_vector)

    def sum(self):
        
        (cols, rows) = self.shape
        sum = 0.
        if (cols == 1):
            for row in range(rows):
                for col in range(cols):
                    sum += self.values[col][row]
        else:
            for col in range(cols):
                for row in range(rows):
                    sum+= self.values[col][row]
        return sum

    def __add__(self, v2):
        """ Performs an addition of a vector by a vector n in all elements of the vector """
        v2 = v2 if isinstance(v2, Vector) and v2.shape == self.shape else None
    
    def __add__(self, n:float):
        """ Performs an addition of a vector by a number n in all elements of the vector """
        sum = lambda row,col: n + self.values[col][row]
        return self.iter(sum)
    
    def __radd__(self, n:float):
        """ Performs an addition of a vector by a number n in all elements of the vector for the right """
        return self.__add__(n)

    def __sub__(self, n: float):
        """ Performs a substraction of a vector by a number n in all elements of the vector """
        return self.__add__(-n)

    def __mul__(self, n: float):
        """" Performs a multiplication of a vector by a number n in all elements of the vector"""
        mul = lambda row, col: n * self.values[col][row]
        return self.iter(mul)
        

    def __rmul__(self, n: float):
        """" Performs a multiplication of a vector by a number n in all elements of the vector for the right """
        return self.__mul__(n)

    def abs(self) -> float:
        """" Returns a module for a vector """
        def squares(a):
            return (a ** 2)
        sq = self.iter(lambda row, col: squares(self.values[col][row]))
        return sq.sum() ** 0.5


    def __truediv__(self, n: float):
        """" Performs a multiplication of a vector by a number n in all elements of the vector"""
        try:
            if (n == 0):
                raise ValueError("ZeroDivisionError: division by zero.")
            return self.iter(lambda row, col: self.values[col][row] / n)
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
        prod_esc = lambda row, col: float(self.values[col][row]) * float(v2.values[col][row])
        return self.iter(prod_esc).sum()
    

    def __str__(self):
        return "Vector({values}) <r={rows}|c={cols}>".format(
            values=self.values,
            rows=self.shape[0],
            cols=self.shape[1]
        )


######################################################################
##
## 🆘 DEBUG AREA
##
######################################################################
##
##
##        v1 = Vector([[1., 3., 3.]])
##        print("Vector([[1., 2., 3.]])", str(v1))
##        n = 2
##        print("{} * {} = {}".format(str(v1), n, str(v1 * n)))
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
##
##
##########################################################################

