def obfuscate(value):
    return ''.join(f'&#{ord(c)};' for c in value)


def obfuscate_mailto(value, text=''):
    mail = obfuscate(value)
    if text:
        link_text = text
        # Detect subject lines
        if ';' in text:
            args = text.split(';', 1)
            link_text = args[0]
            subject = args[1]
            mail = mail + '?subject=' + subject
    else:
        link_text = mail
    return f'<a href="{obfuscate('mailto:')}{mail}">{link_text}</a>'
