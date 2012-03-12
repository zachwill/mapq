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

>>> g.address('123 Any Street')
```
