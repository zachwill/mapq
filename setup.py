"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
Interacting with the Mapquest Geocoding API should be easy.

    >>> import mapq

    >>> mapq.key('my_api_key')

    >>> mapq.address('155 9th St San Francisco, CA')
    [{'lots': {'of': 'results'}}, ...]

    >>> mapq.batch('94103', '1 Infinity Loop Cupertino', 'Yerba Buena Park')
    [{'multiple': 'locations'}, ...]

    >>> mapq.geocode('155 9th St San Francisco, CA')
    {'single': {'geocode': 'result'}}

    >>> mapq.reverse(37.775002, -122.418297)
    {'looks': {'like': '155 9th St'}}

    >>> mapq.latlng('155 9th St San Francisco, CA')
    {'lat': 37.775002, 'lng': -122.418297}
"""


setup(
    name="mapq",
    version="0.3",
    url="http://github.com/zachwill/mapq",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    keywords=['mapquest', 'geocoding', 'google maps', 'geocode'],
    description="An easy-to-use Mapquest Geocoding API wrapper.",
    long_description=long_description,
    packages=[
        'mapq'
    ],
    install_requires=[
        'requests',
        'simplejson',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
