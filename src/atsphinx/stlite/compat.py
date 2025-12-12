"""Compatibility module for Python versions."""

import sys

if sys.version_info < (3, 11):
    import tomli as tomllib  # noqa: F401
else:
    import tomllib  # noqa: F401
