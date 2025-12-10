"""Embed Stlite frame into Sphinx documentation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.writers.html5 import HTML5Translator

__version__ = "0.0.0"


class stlite(nodes.Element, nodes.General):  # noqa: D101
    pass


def visit_stlite(self: HTML5Translator, node: stlite) -> None:  # noqa: D103
    self.body.append('<div class="stlite-wrapper"><iframe class="stlite-frame">')


def depart_stlite(self: HTML5Translator, node: stlite) -> None:  # noqa: D103
    self.body.append("</iframe></div>")


class StliteDirective(SphinxDirective):  # noqa: D101
    has_content = True

    def run(self):  # noqa: D102
        node = stlite()
        if self.content:
            node["code"] = "\n".join(self.content)
        return [node]


def setup(app: Sphinx):  # noqa: D103
    app.add_node(stlite, html=(visit_stlite, depart_stlite))
    app.add_directive("stlite", StliteDirective)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
