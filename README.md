django-email-obfuscator
=======================

A Django template filter to protect email addresses from crawlers.

Installation
------------

Install from the Python package index:

    $ pip install django-email-obfuscator

Add `email_obfuscator` to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = (
    # ...
    'email_obfuscator',
)
```

Usage
-----

In your templates, you can protect email addresses with the `obfuscate`
filter:

```python
{% load email_obfuscator %}
{{ 'your@email.com'|obfuscate }}
```

The email address will be encoded with ASCII character entities, protecting it
from spambots but rendering it readably in web browsers.

You can also use the filter to create clickable `mailto` links:

```python
{% load email_obfuscator %}
{{ 'your@email.com'|obfuscate_mailto }}
#returns '<a href="mailto:your@email.com">your@email.com</a>' as an encoded string like
#<a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#121;&#111;&#117;&#114;&#64;&#101;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">&#121;&#111;&#117;&#114;&#64;&#101;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;</a>
```
