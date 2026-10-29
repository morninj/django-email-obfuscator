from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from . import html_entity
from . import js_concatenation

register = template.Library()


METHODS = {
    'html_entity': html_entity,
    'js_concatenation': js_concatenation,
}

def get_method():
    return getattr(settings, 'EMAIL_OBFUSCATOR_METHOD', 'html_entity')

@register.filter
@stringfilter
def obfuscate(value):
    method = get_method()
    module = METHODS.get(method)
    if module is None:
        raise ValueError(f'Unknown EMAIL_OBFUSCATOR_METHOD: {method!r}')
    return mark_safe(module.obfuscate(value))


@register.filter
@stringfilter
def obfuscate_mailto(value, text=''):
    method = get_method()
    module = METHODS.get(method)
    if module is None:
        raise ValueError(f'Unknown EMAIL_OBFUSCATOR_METHOD: {method!r}')
    return mark_safe(module.obfuscate_mailto(value, text))
