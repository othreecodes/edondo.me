import hashlib
import urllib
from django import template
from django.utils.safestring import mark_safe
import random

register = template.Library()


# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=150):
    default = "https://lh3.googleusercontent.com/-Ybz8OAwoVxg/AAAAAAAAAAI/AAAAAAAAAAA/hNDTT4sTJrw/s181-c/114068962698415999808.jpg"
    return "https://www.gravatar.com/avatar/%s?%s" % (
        hashlib.md5(email.lower().encode('utf-8')).hexdigest(), urllib.parse.urlencode({'d': default, 's': str(size)}))


# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('<img src="%s" height="%d" width="%d">' % (url, size, size))


@register.filter
def get_random_image(request):
    logos = ['12.jpg', '16.jpg', '19.jpg', '27.jpg']
    pos = random.randrange(0, 3)
    return logos[pos]
