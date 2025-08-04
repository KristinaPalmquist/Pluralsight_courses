from django.shortcuts import render
from common.utils import getResults
import dailynews.config as config

links = [
    {"name": "Home", "path": "/"},
    {"name": "Top Stories", "path": "/topstories"},
    {"name": "Most Popular", "path": "/popular"},
    {"name": "Real Time Feed", "path": "/feed"},
]

TOPSTORIES = 'https://api.nytimes.com/svc/topstories/v2/arts.json?api-key='
MOSTPOPULAR = (
    'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key='
)
FEED = 'https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key='


def home(request):
    apis = [
        {"name": "Top Stories API", "path": "/topstories"},
        {"name": "Most Popular API", "path": "/popular"},
        {"name": "Time Wire API", "path": "/feed"},
    ]
    return render(request, 'articles/home.html', {
        'title': 'Daily News',
        "apis": apis,
        "links": links
    })


def results(request):
    pathname = str(request).split("/").pop(1)
    results = []
    subtitle = ""

    if (pathname == "topstories"):
        results = getResults(TOPSTORIES + config.api_key)
        subtitle = "Top"
    elif (pathname == "popular"):
        results = getResults(MOSTPOPULAR + config.api_key)
        subtitle = "Most Popular"
    elif (pathname == "feed"):
        results = getResults(FEED + config.api_key)
        subtitle = "News Feed"
    else:
        return

    return render(request, 'articles/results.html', {
            'title': 'Daily News',
            'subtitle': subtitle,
            'results': results,
            'links': links,
            "pathname": pathname + "/"
        })


# def topstories(request):
#     results = getResults(
#         'https://api.nytimes.com/svc/topstories/v2/home.json?api-key='
#         + config.api_key
#     )
#     return render(request, 'articles/results.html', {
#         'title': 'Daily News',
#         "subtitle": "Top Stories",
#         "results": results,
#         "links": links
#     })


# def popular(request):
#     results = getResults(
#         'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key='
#         + config.api_key
#     )
#     return render(request, 'articles/results.html', {
#         'title': 'Daily News',
#         "subtitle": "Most Popular",
#         "results": results,
#         "links": links
#     })


# def feed(request):
#     results = getResults(
#         'https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key='
#         + config.api_key
#     )
#     return render(request, 'articles/results.html', {
#         'title': 'Daily News',
#         "subtitle": "News Feed",
#         "results": results,
#         "links": links
#     })
