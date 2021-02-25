from pathlib import Path

import pytest

from plainhtml import dom
from plainhtml.core import CLEANER
from plainhtml.utils import parse_tree

TESTCASES_FOLDER = Path(Path(__file__).parent, "testcases")


@pytest.fixture
def html():
    with Path(TESTCASES_FOLDER, "snapaddy_imprint.html").open("r") as f:
        return f.read().strip()


@pytest.fixture
def text():
    with Path(TESTCASES_FOLDER, "snapaddy_imprint.txt").open("r") as f:
        return f.read().strip()


def test_dom(html, text):
    tree = parse_tree(html)
    clean_tree = CLEANER.clean_html(tree)
    assert dom.DOM(clean_tree).extract_text() == text
