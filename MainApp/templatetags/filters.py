# Django imports
from django import template

register = template.Library()


@register.filter
def image_300(image_url):
    """
    Given an image URL image for 100x100, make it for 300x300 size and return it
    :param image_url: url for 100x100 size
    :return: updated image url for 300x300 size
    """
    url_array = image_url.split('/')
    url_array[-1] = url_array[-1].replace('1', '3')
    return '/'.join(url_array)


