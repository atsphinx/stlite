"""Embed Stlite frame into Sphinx documentation."""

from __future__ import annotations

from html import escape
from pathlib import Path
from typing import TYPE_CHECKING

from docutils import nodes
from jinja2 import Template
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.writers.html5 import HTML5Translator

__version__ = "0.0.0"

__here = Path(__file__).parent

srcdoc_template = Template((__here / "frame.html.jinja").read_text(encoding="utf-8"))


class stlite(nodes.Element, nodes.General):  # noqa: D101
    pass


def visit_stlite(self: HTML5Translator, node: stlite) -> None:  # noqa: D103
    config = self.builder.config
    srcdoc = escape(srcdoc_template.render(node.attributes, config=config))
    self.body.append(
        f'<div class="stlite-wrapper"><iframe class="stlite-frame" srcdoc="{srcdoc}">'
    )


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
    app.add_config_value("stlite_default_version", "latest", "env", str)
    app.add_node(stlite, html=(visit_stlite, depart_stlite))
    app.add_directive("stlite", StliteDirective)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
