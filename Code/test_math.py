import pytest
from hexaware_sample.day3_1 import addition, get_multiplication_table

def test_add():
    assert addition(1,1) == 2
    assert addition(2,1) == 3
    assert addition(12,12) == 24
    assert addition(1,21) == 22

def test_mul():
    assert get_multiplication_table(2,3) == 6





pytest
pytest -v
pytest tests
pytest tests/test_math.py
pytest tests/test_math.py::test_add
pytest -k 'mu'