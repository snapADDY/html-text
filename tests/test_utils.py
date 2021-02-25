from lxml.html import HtmlElement

from plainhtml import utils


def test_parse_tree():
    tree = utils.parse_tree("<html><body>Hi</body></html>")
    assert isinstance(tree, HtmlElement)
    assert len(tree) == 1
