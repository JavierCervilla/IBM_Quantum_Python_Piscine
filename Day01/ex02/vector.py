# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javier <javier@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 13:38:34 by javier            #+#    #+#              #
#    Updated: 2023/03/15 17:29:25 by javier           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import colors
from math import sqrt, cos

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
        

v1 = Vector([[1., 2., 3.]])
n = 2.
print("{} + {} = {}".format(str(v1), n, str(v1 + n)))
print("{} * {} = {}".format(str(v1), n, str(v1 * n)))
print("{} * {} = {}".format(n, str(v1), str(n * v1)))
print("{} / {} = {}".format(str(v1), n, str(v1 / n)))
#print("{} / {} = {}".format(n, str(v1, str(n / v1))))
print("{} / {} = {}".format(str(v1), 0, str(v1 / 0)))

print(v1.abs())

v2 = Vector([[1.], [2.], [3.]])
print("{} * {} = {}".format(str(v2), n, str(v2 * n)))
print("{} * {} = {}".format(n, str(v2), str(n * v2)))
print("{} / {} = {}".format(str(v2), n, str(v2 / n)))
#print("{} / {} = {}".format(n, str(v2, str(n / v2))))
print("{} / {} = {}".format(str(v2), 0, str(v2 / 0)))

print(v2.abs())


""" v2 = Vector([[1.], [2.], [3.]])
print(str(v2))
m1 = Vector([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
print(str(m1)) """

