import pytest

from src.main import hello

def test_hello():
    expected = "Hello world!"
    actual = hello()
    assert actual == expected
