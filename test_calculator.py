import pytest
from calculator import add, subtract, multiply, divide
from main import evaluate

def test_add_positive():
    assert add(6, 4) == 10
    
def test_add_negative():
    assert add(-12, -5) == -17
    
def test_subtract_positive():
    assert subtract(10, 3) == 7
    
def test_subtract_negative():
    assert subtract(-8, -2) == -6
    
def test_multiply_positive():
    assert multiply(7, 5) == 35
    
def test_multiply_negative():
    assert multiply(-3, 4) == -12
    
def test_multiply_by_zero():
    assert multiply(9, 0) == 0
    
def test_divide_positive():
    assert divide(20, 4) == 5
    
def test_divide_negative():
    assert divide(-15, 3) == -5
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
        
def test_divide_float_result():
    assert divide(9, 2) == 4.5
    
def test_evaluate_add():
    assert evaluate("12 + 3.5") == 15.5
    
def test_evaluate_bad_format():
    with pytest.raises(ValueError):
        evaluate("1 +")