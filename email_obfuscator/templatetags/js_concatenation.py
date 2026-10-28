import zlib


def _js_hash(value):
    """Non-cryptographic hash; just identifies elements within one page."""
    return format(zlib.crc32(value.encode('utf-8')) & 0xffffffff, '08x')


def _js_quote(value):
    """Render as 'f' + 'o' + 'o' concatenation."""
    return ' + '.join(f"'{c}'" for c in value)


def _js_escape(value):
    return value.replace('\\', '\\\\').replace("'", "\\'")


def _js_script(value, hash, body):
    return f'''
<script type="module">
const email = {_js_quote(value)};
document.querySelectorAll(
    '.obfuscated-email[data-hash="{hash}"]'
).forEach(a => {{{body}}});
</script>
'''.strip()


def obfuscate(value, tag='span'):
    """
    https://spencermortensen.com/articles/email-obfuscation/#link-concatenation
    """
    hash = _js_hash(value)
    body = '        a.replaceWith(document.createTextNode(email));'
    script = _js_script(value, hash, body)
    return f'<{tag} class="obfuscated-email" data-hash="{hash}"></{tag}>\n{script}'


def obfuscate_mailto(value, text='', attrs=''):
    hash = _js_hash(value)
    href_expr = "'mailto:' + email"
    if text != '':
        link_text = text
        if ';' in text:
            link_text, subject = text.split(';', 1)
            href_expr += " + '" + _js_escape('?subject=' + subject) + "'"
    else:
        link_text = None
    text_expr = f"'{_js_escape(link_text)}'" if link_text is not None else 'email'
    body = (f"        a.setAttribute('href', {href_expr});\n"
            f"        a.textContent = {text_expr};")
    script = _js_script(value, hash, body)
    attr_str = ' ' + attrs.strip() if attrs else ''
    return f'<a class="obfuscated-email" data-hash="{hash}"{attr_str}></a>\n{script}'
