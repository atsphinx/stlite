"""Standard tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp):
    """Test to pass."""
    app.build()
    html = app.outdir / "index.html"
    soup = BeautifulSoup(html.read_text(), "html.parser")
    assert soup.find("iframe")
