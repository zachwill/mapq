"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="mapq",
    version="0.2.1",
    url="http://github.com/zachwill/mapq",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    description="An easy-to-use Mapquest Geocoding API wrapper.",
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
