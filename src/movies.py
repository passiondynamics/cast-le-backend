import requests

def popular_movies():
    # number of pages of popular movies to get there are 20 results on each page
    pages = 1
    # api endpoint
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page={}&region=US".format(pages)

    # api header for authorization
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWNhNjRiOGE1ZGM4OWZlNTNmNzQ5Y2I4MDAwMGIxMSIsInN1YiI6IjY1YjAwMWJhNjdiNjEzMDBlYjUzODA2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B5tu8C5pXbVtxrfR0aPJgqLu0povlRhuf1a8T7sWDjk"
    }

    # use the api url and headers to get the information on the popular movies
    response = requests.get(url, headers=headers)
    print(response.status_code)

def toprated_movies():
    # number of pages of top rated movies to get there are 20 results on each page
    pages = 1
    # api endpoint
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={}&region=US".format(pages)

    # api header for authorization
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWNhNjRiOGE1ZGM4OWZlNTNmNzQ5Y2I4MDAwMGIxMSIsInN1YiI6IjY1YjAwMWJhNjdiNjEzMDBlYjUzODA2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B5tu8C5pXbVtxrfR0aPJgqLu0povlRhuf1a8T7sWDjk"
    }

    # use the api url and headers to get the information on the popular movies
    response = requests.get(url, headers=headers)
    print(response.status_code)