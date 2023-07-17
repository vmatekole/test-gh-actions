from src.calculator import add
import pytest

def test_add():
    assert add(1, 2) == 2
    assert add(-2, 2) == 0
    assert add(0, 0) == 0