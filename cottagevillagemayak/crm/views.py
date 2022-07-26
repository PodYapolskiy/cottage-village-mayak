from django.shortcuts import render
from django.template.defaulttags import register


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
    return render(request, './index.html')


def about_page(request):
    return render(request, './about.html')
