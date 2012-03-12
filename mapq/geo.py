"""
Geocode locations using the Mapquest Geocoding API.

Documentation:  http://www.mapquestapi.com/geocoding/
"""

import os
import requests as req
from simplejson import loads


class Geo(object):
    """A simple Mapquest Geocoding API wrapper."""

    def __init__(self, api_key=None):
        if not api_key:
            if 'MAPQUEST_API_KEY' in os.environ:
                self.api_key = os.environ['MAPQUEST_API_KEY']
            else:
                self.api_key = ''
        else:
            self.api_key = api_key
        self.endpoint = "http://www.mapquestapi.com/geocoding/v1"

    def get(self, path, **kwargs):
        """Perform a get request."""
        url = '/'.join((self.endpoint, path))
        kwargs['key'] = self.api_key
        request = req.get(url, params=kwargs)
        self.request = request
        results = loads(request.text)['results']
        return results

    def address(self, name, **kwargs):
        """Geocode an address."""
        kwargs['location'] = name
        return self.get('address', **kwargs)
