from calculator import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 3) == 7