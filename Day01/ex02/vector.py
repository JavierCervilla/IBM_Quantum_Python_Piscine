# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javier <javier@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 13:38:34 by javier            #+#    #+#              #
#    Updated: 2023/03/15 20:23:29 by javier           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import sqrt, cos
from utils import colors

# COLUMNA: ([[1., 2., 3.]])
# FILA: ([[1.], [2.], [3.]])

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
    
    def map(self, func):
        (cols, rows) = self.shape
        new_vector = list()
        if (cols == 1):
            for col in range(cols):
                new_row = list()
                for row in range(rows):
                    new_col = func(self.values[col][row])
                    new_row.append(new_col)
                new_vector.append(new_row)
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

    #def __sub__(self, p2):
    #    pass

    def __mul__(self, n: float):
        """"Performs a scalar multiplication of a vector by a number n"""
        mul = lambda a: n * a 
        return self.map(mul)

    def __rmul__(self, n: float):
        return self.__mul__(n)

    def abs(self) -> float:
        def squares(a):
            return (a ** 2)
        sq = self.map(lambda a: squares(a))
        print(str(sq))
        return sq.sum()
        return self.sum()


    def __truediv__(self, n: float):
        try:
            if (n == 0):
                raise ValueError("ZeroDivisionError: division by zero.")
            div = lambda a: a * n
            return self.map(div)
        except Exception as error:
            self.__error__(error=error)

    def __error__(self, error):
        print("{red}Error: {error}{reset}".format(
            error=error,
            red=colors["red"],
            reset=colors["reset"]
        ))

    def __rtruediv__(self, n: float):
        try:
            raise Exception("NotImplementedError: Division of a scalar by a Vector is not defined here.")
        except Exception as error:
            self.__error__(error=error)
            
    
    
    def __str__(self):
        return "Vector({values}) <r={rows}|c={cols}>".format(
            values=self.values,
            rows=self.shape[0],
            cols=self.shape[1]
        )

## v1 = Vector([[1., 2., 3.]])
## print("Vector([[1., 2., 3.]])", str(v1))
## n = 2
## print("{} * {} = {}".format(str(v1), n, str(v1 * n)))
## print("{} * {} = {}".format(n, str(v1), str(n * v1)))
## print("{} / {} = {}".format(str(v1), n, str(v1 / n)))
## print("{} / {} = {}".format(str(v1), 0, str(v1 / 0)))
## print(v1.abs())
## 
## v1 = Vector([[1.], [2.],[3.]])
## print("Vector([[1.], [2.],[3.]])", str(v1))
## 
## print("{} * {} = {}".format(str(v1), n, str(v1 * n)))
## print("{} * {} = {}".format(n, str(v1), str(n * v1)))
## print("{} / {} = {}".format(str(v1), n, str(v1 / n)))
## print("{} / {} = {}".format(str(v1), 0, str(v1 / 0)))
## print(v1.abs())
