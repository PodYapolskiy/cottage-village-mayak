from django.shortcuts import render
from django.template.defaulttags import register

# from django.conf import settings


@register.filter
def get_range(value):
    """Custom jinja filter that accepts usage of range loop in jinja.

    Args:
        value int: number of iterations

    Returns:
        range: range object

    Example:
        >>> {% for i in 5|get_range %}
        >>>     {{ i }}
        >>> {% endfor %}

    Result:
        >>> 0
        >>> 1
        >>> 2
        >>> 3
        >>> 4
    """
    return range(value)


def index_page(request):
    # url = str(settings.STATICFILES_DIRS[0]) + "\img\main.jpg"
    url = "static/img/main.jpg"
    print(url)
    return render(request, './index.html', {
        "news": {
            "1": {
                "url": url,
                "title": "Рекордная жара не спадает",
                "date": "12 июня 2022",
            },
            "2": {
                "url": "static/img/about_1.jpg",
                "title": "Кудри стали круче",
                "date": "16 июня 2022",
            },
            "3": {
                "url": "static/img/about_2.jpg",
                "title": "Местные приняли",
                "date": "12 июня 2022",
            },
        }
    })


def about_page(request):
    return render(request, './about.html')
