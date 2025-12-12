"""Nodes and translators."""

from __future__ import annotations

from html import escape
from pathlib import Path
from typing import TYPE_CHECKING

from docutils import nodes
from jinja2 import Template
from sphinx.util import logging

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.writers.html5 import HTML5Translator

logger = logging.getLogger(__name__)
srcdoc_template = Template(
    (Path(__file__).parent / "frame.html.jinja").read_text(encoding="utf-8")
)


class stlite(nodes.Element, nodes.General):  # noqa: D101
    pass


def visit_stlite(self: HTML5Translator, node: stlite) -> None:  # noqa: D103
    config = self.builder.config
    srcdoc = escape(srcdoc_template.render(app=node.attributes, config=config))
    self.body.append(
        f'<div class="stlite-wrapper"><iframe class="stlite-frame" srcdoc="{srcdoc}">'
    )


def depart_stlite(self: HTML5Translator, node: stlite) -> None:  # noqa: D103
    self.body.append("</iframe></div>")


def _setup(app: Sphinx):  # noqa: D103
    app.add_node(stlite, html=(visit_stlite, depart_stlite))
