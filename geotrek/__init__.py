from __future__ import absolute_import

pkg_resources = __import__('pkg_resources')
distribution = pkg_resources.get_distribution('geotrek')

#: Module version, as defined in PEP-0396.
__version__ = distribution.version
