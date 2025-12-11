"""Parser tests."""

from __future__ import annotations

from textwrap import dedent
from typing import TYPE_CHECKING

import pytest
from atsphinx.stlite.nodes import stlite
from sphinx.testing import restructuredtext

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(confoverrides={"extensions": ["atsphinx.stlite"]})
def test__parse_content_source(app: SphinxTestApp):
    """Test to pass."""
    source = """
    .. stlite::

       import streamlit as st

       st.title("Hello world")
    """
    doctree = restructuredtext.parse(app, dedent(source).strip())
    nodes = list(doctree.findall(stlite))
    assert len(nodes) == 1
    assert "code" in nodes[0]
    assert nodes[0]["code"] == 'import streamlit as st\n\nst.title("Hello world")'


@pytest.mark.sphinx(confoverrides={"extensions": ["atsphinx.stlite"]})
def test__parse_json_config(app: SphinxTestApp):
    """Test to pass."""
    source = """
    .. stlite::
       :config: {"client": {"toolbarMode": "viewer"}}

       print("Hello world")
    """
    doctree = restructuredtext.parse(app, dedent(source).strip())
    nodes = list(doctree.findall(stlite))
    assert len(nodes) == 1
    assert "code" in nodes[0]
    assert nodes[0]["config"] == {"client": {"toolbarMode": "viewer"}}


@pytest.mark.sphinx(confoverrides={"extensions": ["atsphinx.stlite"]})
def test__parse_toml_config(app: SphinxTestApp):
    """Test to pass."""
    source = """
    .. stlite::
       :config:
         [client]
         toolbarMode = "viewer"

       print("Hello world")
    """
    doctree = restructuredtext.parse(app, dedent(source).strip())
    nodes = list(doctree.findall(stlite))
    assert len(nodes) == 1
    assert "code" in nodes[0]
    assert nodes[0]["config"] == {"client": {"toolbarMode": "viewer"}}
