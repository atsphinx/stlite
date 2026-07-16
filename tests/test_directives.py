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


@pytest.mark.sphinx(confoverrides={"extensions": ["atsphinx.stlite"]})
@pytest.mark.parametrize(
    ["source"],
    [
        pytest.param(
            """
    .. stlite::
       :requirements: matplotlib, polars

       print("Hello world")
    """,
            id="comma-splitted",
        ),
        pytest.param(
            """
    .. stlite::
       :requirements:
         matplotlib
         polars

       print("Hello world")
    """,
            id="multiline",
        ),
    ],
)
def test__parse_requirements(app: SphinxTestApp, source: str):
    """Test to pass."""
    doctree = restructuredtext.parse(app, dedent(source).strip())
    node = pick_first_stlite(doctree)
    assert node["requirements"] == ["matplotlib", "polars"]


@pytest.mark.sphinx(confoverrides={"extensions": ["atsphinx.stlite"]})
@pytest.mark.parametrize(
    ["source", "expected"],
    [
        pytest.param(
            """
    .. stlite::
       :width: 500px

       print("Hello world")
    """,
            "500px",
            id="with-unit",
        ),
        pytest.param(
            """
    .. stlite::
       :width: 30rem

       print("Hello world")
    """,
            "30rem",
            id="rem-unit",
        ),
        pytest.param(
            """
    .. stlite::
       :width: 600

       print("Hello world")
    """,
            "600",
            id="numeric-only",
        ),
    ],
)
def test__parse_width(app: SphinxTestApp, source: str, expected: str):
    """Test width option parsing."""
    doctree = restructuredtext.parse(app, dedent(source).strip())
    node = pick_first_stlite(doctree)
    assert node["width"] == expected


@pytest.mark.sphinx(confoverrides={"extensions": ["atsphinx.stlite"]})
@pytest.mark.parametrize(
    ["source", "expected"],
    [
        pytest.param(
            """
    .. stlite::
       :height: 500px

       print("Hello world")
    """,
            "500px",
            id="with-unit",
        ),
        pytest.param(
            """
    .. stlite::
       :height: 30rem

       print("Hello world")
    """,
            "30rem",
            id="rem-unit",
        ),
        pytest.param(
            """
    .. stlite::
       :height: 600

       print("Hello world")
    """,
            "600",
            id="numeric-only",
        ),
    ],
)
def test__parse_height(app: SphinxTestApp, source: str, expected: str):
    """Test height option parsing."""
    doctree = restructuredtext.parse(app, dedent(source).strip())
    node = pick_first_stlite(doctree)
    assert node["height"] == expected
