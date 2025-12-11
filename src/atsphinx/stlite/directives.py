"""Directives and option handlers."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

from . import nodes
from .compat import tomllib

if TYPE_CHECKING:
    from sphinx.application import Sphinx

logger = logging.getLogger(__name__)


def parsed_dict(argument: str | None) -> dict | None:
    """Check if the argument is a valid JSON or TOML string."""
    if not argument:
        return None
    try:
        return json.loads(argument)
    except json.JSONDecodeError:
        logger.debug("Failed to parse as JSON. Try parsing as TOML")
        return tomllib.loads(argument)
    except tomllib.TOMLDecodeError as e:
        raise ValueError(f"Invalid value neigher JSON nor TOML: {argument}") from e


class StliteDirective(SphinxDirective):  # noqa: D101
    has_content = True
    option_spec = {
        "config": parsed_dict,
    }

    def run(self):  # noqa: D102
        node = nodes.stlite()
        print(node.attributes, self.options)
        node.attributes |= {"config": None}
        node.attributes |= self.options
        print(node.attributes, self.options)
        if self.content:
            node["code"] = "\n".join(self.content)
        return [node]


def _setup(app: Sphinx):  # noqa: D103
    app.add_directive("stlite", StliteDirective)
