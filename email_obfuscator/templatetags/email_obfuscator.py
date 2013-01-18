from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

def obfuscate_string(value):
    return ''.join(['&#%s;' % str(ord(char)) for char in value])


@register.filter()
@stringfilter
def obfuscate(value):
    return mark_safe(obfuscate_string(value))

@register.filter()
@stringfilter
def obfuscate_mailto(value):
    mail = obfuscate_string(value)
    return mark_safe('<a href="%s%s">%s</a>' % (obfuscate_string('mailto:'), mail, mail))