"""Directives and option handlers."""

from __future__ import annotations

import itertools
import json
from pathlib import Path
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


def list_of_str(argument: str | None) -> list[str] | None:
    """Check if the argument is a valid list of strings."""
    if not argument:
        return None
    values = [value.split(",") for value in argument.split("\n") if value.strip()]
    return [v.strip() for v in itertools.chain.from_iterable(values) if v]


class StliteDirective(SphinxDirective):  # noqa: D101
    optional_arguments = 1
    has_content = True
    option_spec = {
        "config": parsed_dict,
        "requirements": list_of_str,
    }
    DEFAULT_OPTIONS = {
        "config": None,
        "requirements": [],
    }

    def run(self):  # noqa: D102
        node = nodes.stlite()
        node.attributes |= self.DEFAULT_OPTIONS
        node.attributes |= self.options
        if self.arguments:
            source_path = self.state.document["source"]
            app_file = Path(source_path).parent / self.arguments[0]
            if not app_file.exists():
                raise ValueError(f"File not found: {app_file}")
            node["code"] = app_file.read_text()
        elif self.content:
            node["code"] = "\n".join(self.content)
        return [node]


def _setup(app: Sphinx):  # noqa: D103
    app.add_directive("stlite", StliteDirective)
