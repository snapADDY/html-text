from pathlib import Path

import pytest

from plainhtml import core

TESTCASES_FOLDER = Path(Path(__file__).parent, "testcases")


@pytest.fixture
def html():
    with Path(TESTCASES_FOLDER, "snapaddy_imprint.html").open("r") as f:
        return f.read().strip()


@pytest.fixture
def text():
    with Path(TESTCASES_FOLDER, "snapaddy_imprint.txt").open("r") as f:
        return f.read().strip()


def test_extract_text(html, text):
    assert core.extract_text("") == ""
    assert core.extract_text(html) == text
