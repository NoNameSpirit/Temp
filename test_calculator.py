from calculator import add, multiply, subtract

def test_add():
    assert add(2, 3)  == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(5, 5)  == 0