import pytest

from src.main import popular_movies
from src.main import toprated_movies

def test_popular_movies():
    expected = "200"
    actual = popular_movies()
    assert actual == expected

def test_toprated_movies():
    expected = "200"
    actual = toprated_movies()
    assert actual == expected