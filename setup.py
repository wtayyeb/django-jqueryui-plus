
from setuptools import setup, find_packages
from os.path import join, dirname

try:
    f = open(join(dirname(__file__), 'LONG.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name			='django-jqueryui-plus',
    version			='1.11.4.3',
    url				="http://github.com/wtayyeb/django-jqueryui-plus",
    description		='jQuery UI packaged in an handy django app to speed up new applications and deployment.',
    long_description=long_description,
    author			='wtayyeb',
    author_email	='wtayyeb@gmail.com',
    license			='MIT',
    keywords		='django jqueryui staticfiles templatetags',
    platforms		='any',
    classifiers		=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages		=find_packages(),
    include_package_data =True,
    zip_safe		=False,
	install_requires=['django-appconf', ],
)
