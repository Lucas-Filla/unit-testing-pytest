import pytest
from ..calculator import modulo, max, min, power, abs_val, sqrt, is_odd, is_even, is_positive, is_negative


def test_modulo():
    """Verify modulo works with normal operands and throws error at a mod 0"""
    #verifies normal positive behavior
    assert modulo(10, 2) == 0
    #verifies normal negative behavior
    assert modulo(5, -2) == -1
    #verifies for modulo 0 (undefined behavior)
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        modulo(10, 0)

def test_power():
    """Verify that powers work when ints, zero, and floats"""
    #verifies normal case
    assert power(2, 3) == 8
    #verifies power of 0 (always 1)
    assert power(7, 0) == 1
    #verifies a float power (root)
    assert power(9, 0.5) == 3

def test_abs_val():
    """Verify that abs_valolute value works when neg, zero, and pos"""
    #verifies negative to positive
    assert abs_val(-5) == 5
    #verifies zero
    assert abs_val(0) == 0
    #verifies positive stays positive
    assert abs_val(2.5) == 2.5

def test_sqrt():
    """Verify that square root works when positive, zero, and negative raises error"""
    #verifies normal case
    assert sqrt(9) == 3
    #verifies zero case
    assert sqrt(0) == 0
    #verifies negative (imaginary number)
    with pytest.raises(ValueError):
        sqrt(-1)

def test_max():
    """Verify that max works when proper, when equal, and when close floats"""
    #verifies normal behavior
    assert max(10, 3) == 10
    #verifies equal nums
    assert max(5, 5) == 5
    #verifies close float values
    assert max(2.7, 2.71) == 2.71

def test_min():
    """Verify that min works when proper, when equal, and when close floats"""
    #verifies normal behavior
    assert min(10, 3) == 3
    #verifies equal nums
    assert min(5, 5) == 5
    #verifies close float values
    assert min(2.7, 2.71) == 2.7

def test_is_even():
    """Verify that is_even works when even, odd, and zero"""
    #verifies basic true
    assert is_even(8) is True
    #verifies basic false
    assert is_even(7) is False
    #verifies zero case
    assert is_even(0) is True

def test_is_odd():
    """Verify that is_odd works when even, odd, and zero"""
    #verifies basic true
    assert is_odd(9) is True
    #verifies basic false
    assert is_odd(6) is False
    #verifies zero case
    assert is_odd(-3) is True

def test_is_positive():
    """Verify that is_positive correctly recognizes positive numbers, zeros, and negatives"""
    #verifies positive results true
    assert is_positive(1) is True
    #verifies 0 results false
    assert is_positive(0) is False
    #verifies negative results false
    assert is_positive(-1) is False
    
def test_is_negative():
    """Verify that is_negative correctly recognizes positive numbers, zeros, and negatives"""
    #verifies positive results false
    assert is_negative(1) is False
    #verifies 0 results false
    assert is_negative(0) is False
    #verifies negative results true
    assert is_negative(-1) is True
