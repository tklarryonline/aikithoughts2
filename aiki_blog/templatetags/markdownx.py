from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from markdownx.utils import markdownify

register = template.Library()


@register.filter
@stringfilter
def markdownxify(text):
    return mark_safe(markdownify(text))
