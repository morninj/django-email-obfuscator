from setuptools import setup

setup(name='django-email-obfuscator',
    version='0.2.0',
    description='A Django template filter to protect email addresses from \
    crawlers.',
    author='Joseph Mornin',
    author_email='joseph@mornin.org',
    url='https://github.com/morninj/django-email-obfuscator',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    packages=['email_obfuscator'],
    package_data = {
        'email_obfuscator': [
            'templatetags/*',
        ],
    },
    )
