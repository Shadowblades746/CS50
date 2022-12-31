from pytest import raises
from fuel import convert, gauge

def test_random():
    assert gauge(69) == "69%"

def test_empty():
    assert gauge(1) == "E"

def test_full():
    assert gauge(99) == "F"

def test_value_error():
    with raises(ValueError):
        convert('six/nine')

def test_zero_division_error():
    with raises(ZeroDivisionError):
        convert('0/0')

def test_converter():
    assert convert('6/9') ==  67


