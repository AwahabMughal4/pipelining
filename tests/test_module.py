import pytest
from my_module import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(2, 2) == 0

if __name__ == "__main__":
    pytest.main()
