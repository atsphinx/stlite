"""Parser tests."""

from __future__ import annotations

from textwrap import dedent
from typing import TYPE_CHECKING

import pytest
from atsphinx.stlite.nodes import stlite
from docutils.nodes import document
from sphinx.testing import restructuredtext

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


def pick_first_stlite(doctree: document) -> stlite:
    nodes = list(doctree.findall(stlite))
    assert len(nodes) == 1
    return nodes[0]


@pytest.mark.sphinx(confoverrides={"extensions": ["atsphinx.stlite"]})
def test__parse_content_source(app: SphinxTestApp):
    """Test to pass."""
    source = """
    .. stlite::

       import streamlit as st

       st.title("Hello world")
    """
    doctree = restructuredtext.parse(app, dedent(source).strip())
    node = pick_first_stlite(doctree)
    assert "code" in node
    assert node["code"] == 'import streamlit as st\n\nst.title("Hello world")'


@pytest.mark.sphinx(confoverrides={"extensions": ["atsphinx.stlite"]})
@pytest.mark.parametrize(
    ["source"],
    [
        pytest.param(
            """
    .. stlite::
       :config: {"client": {"toolbarMode": "viewer"}}

       print("Hello world")
    """,
            id="json",
        ),
        pytest.param(
            """
    .. stlite::
       :config:
         [client]
         toolbarMode = "viewer"

       print("Hello world")
    """,
            id="toml",
        ),
    ],
)
def test__parse_config(app: SphinxTestApp, source: str):
    """Test to pass."""
    doctree = restructuredtext.parse(app, dedent(source).strip())
    node = pick_first_stlite(doctree)
    assert node["config"] == {"client": {"toolbarMode": "viewer"}}
