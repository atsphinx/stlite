"""Embed Stlite frame into Sphinx documentation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sphinx.util import logging

from . import directives, nodes

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__version__ = "0.2.1"

logger = logging.getLogger(__name__)


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("stlite_default_version", "latest", "env", str)
    nodes._setup(app)
    directives._setup(app)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
