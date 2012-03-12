mapq
====

An easy-to-use wrapper for the [Mapquest Geocoding API](http://www.mapquestapi.com/geocoding/).


Installation
------------

    pip install mapq


Usage
-----

```python
>>> from mapq import Geo
>>> g = Geo('my_api_key')

>>> g.address('155 9th St San Francisco, CA')
[{'lots': {'of': 'results'}}, ...]

>>> g.reverse(37.775002, -122.418297)
{'looks': {'like': '155 9th St San Francisco, CA'}}

>>> g.latlng('155 9th St San Francisco, CA')
{'lat': 37.775002, 'lng': -122.418297}
```
