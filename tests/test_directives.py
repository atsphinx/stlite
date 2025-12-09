"""Parser tests."""

from __future__ import annotations

from textwrap import dedent
from typing import TYPE_CHECKING

import atsphinx.stlite as T
import pytest
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
    nodes = list(doctree.findall(T.stlite))
    assert len(nodes) == 1
    assert "code" in nodes[0]
    assert nodes[0]["code"] == 'import streamlit as st\n\nst.title("Hello world")'
