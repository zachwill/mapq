"""
Simplified methods for calling Mapquest's Geocoding API.
"""

from .geo import Geo


def address(name, **kwargs):
    """Geocode an address."""
    return Geo().address(name, **kwargs)


def batch(*locations, **kwargs):
    """Batch geocode multiple addresses."""
    return Geo().batch(*locations, **kwargs)


def geocode(address, **kwargs):
    """Return first the geocode result for a given address."""
    return Geo().address(address, **kwargs)[0]


def latlng(address, **kwargs):
    """Get the latitude and longitude coordinates for an address."""
    return Geo().latlng(address, **kwargs)


def reverse(lat, lng, **kwargs):
    """Reverse geocode lat/lng coordinates."""
    return Geo().reverse(lat, lng, **kwargs)
