import pytest

from src.main import hello

def test_hello():
    expected = "bello world!"
    actual = hello()
    assert actual == expected
