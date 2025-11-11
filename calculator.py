import math
#simple calculator app functions (beyond add, subtract, multiply, divide)
def modulo(a:int | float, b: int | float):
    """
    Return the modulo of a by b
    Raises:
        ValueError: If b is zero.
    """
    if(b == 0):
        raise ValueError("Cannot modulo by zero")
    return a % b

def power(a:int | float, b: int | float):
    """Return the exponent result of a to the power of b"""
    return pow(a, b)

def abs_val(a:int | float):
    """Return the absolute value of a number"""
    return abs(a)

def sqrt(a:int | float):
    """Return the square root of a number"""
    if(a < 0):
        raise ValueError("Cannot take square root of negative")
    return math.sqrt(a)

def max(a:int | float, b: int | float):
    """Return the max of two numbers"""
    if a > b:
        return a
    return b

def min(a:int | float, b: int | float):
    """Return the min of two numbers"""
    if a > b:
        return b
    return a

def is_even(n: int):
    """Return True if n is even."""
    return n % 2 == 0

def is_odd(n: int):
    """Return True if n is odd."""
    return n % 2 != 0

def is_positive(a: int | float):
    """Return True if a is positive."""
    return a > 0

def is_negative(a: int | float):
    """Return True if a is negative."""
    return a < 0
