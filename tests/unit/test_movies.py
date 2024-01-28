import pytest
import json
import src.movies

def test_popular_movies():
    # api authorization
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWNhNjRiOGE1ZGM4OWZlNTNmNzQ5Y2I4MDAwMGIxMSIsInN1YiI6IjY1YjAwMWJhNjdiNjEzMDBlYjUzODA2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B5tu8C5pXbVtxrfR0aPJgqLu0povlRhuf1a8T7sWDjk"
    }

    with open('popular_movies.json', 'r', encoding='utf-8') as json_file:
        # load content
        json_content = json.load(json_file)

    actual = src.movies.popular_movies(1, headers)
    assert actual[0]['title'] == json_content[0]['title']
    assert actual[1]['title'] == json_content[1]['title']
    assert actual == json_content

def test_toprated_movies():
    # api authorization
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWNhNjRiOGE1ZGM4OWZlNTNmNzQ5Y2I4MDAwMGIxMSIsInN1YiI6IjY1YjAwMWJhNjdiNjEzMDBlYjUzODA2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B5tu8C5pXbVtxrfR0aPJgqLu0povlRhuf1a8T7sWDjk"
    }

    with open('toprated_movies.json', 'r', encoding='utf-8') as json_file:
        # load content
        json_content = json.load(json_file)

    actual = src.movies.popular_movies(1, headers)
    assert actual[0]['title'] == json_content[0]['title']
    assert actual[1]['title'] == json_content[1]['title']
    assert actual == json_content

def test_actors():
    # api authorization
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWNhNjRiOGE1ZGM4OWZlNTNmNzQ5Y2I4MDAwMGIxMSIsInN1YiI6IjY1YjAwMWJhNjdiNjEzMDBlYjUzODA2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B5tu8C5pXbVtxrfR0aPJgqLu0povlRhuf1a8T7sWDjk"
    }

    with open('toprated_movies.json', 'r', encoding='utf-8') as json_file:
        # load content
        json_content = json.load(json_file)

