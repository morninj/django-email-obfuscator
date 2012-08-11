from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def obfuscate(value):
    obfuscated_string = ''
    for character in value:
        obfuscated_string = obfuscated_string + '&#' + str(ord(character)) + ';'
    return obfuscated_string

