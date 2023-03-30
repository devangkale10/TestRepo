"""This is a python script that will be used as a calculator. 
It will be able to add, subtract, multiply, divide, find the remainder, negate, square, cube, 
and check if a number is even."""
"""Author: Devang Kale
    Date: 29/03/2023
    Version: 1.0.0
    Python Version: 3.9.2
"""

# add two numbers
def addNums(a, b):
    return a + b


# multiply two numbers
def multiplyNums(a, b):
    return a * b


# subtract two numbers
def subtractNums(a, b):
    return a - b


# divide two numbers
def divideNums(a, b):
    return a / b


# remainder of two numbers
def remainderNums(a, b):
    return a % b


# negate a number
def negateNums(a):
    return -a


# square a number
def squareNums(a):
    return a * a


# cube a number
def cubeNums(a):
    return a * a * a


# is a number even?
def isEven(a):
    return a % 2 == 0


def main():
    print(addNums(5, 4))
    print(multiplyNums(5, 4))
    print(subtractNums(5, 4))
    print(divideNums(5, 4))
    print(remainderNums(5, 4))
    print(negateNums(5))
    print(squareNums(5))
    print(cubeNums(5))
