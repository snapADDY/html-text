# Extract plain text from HTML

How is `plainhtml` different from `.xpath("//text()")` from `lxml` or `.get_text()` from `bs4`?

- Text extracted with `plainhtml` does not contain inline styles, JavaScript, comments and other text that is not normally visible to users
- `plainhtml` normalizes whitespace, but in a way smarter than `.xpath("normalize-space()")`, adding spaces around inline elements (which are often used as block elements in HTML), and trying to avoid adding extra spaces for punctuation
- `plainhtml` can add newlines (e.g. after headers or paragraphs), so that the output text looks more like how it is rendered in browsers

## Installation

```
$ pip install plainhtml
```

## Example

```python
>>> import plainhtml
>>> html = "<html><body><p>foo</p><p>bar</p></body></html>"
>>> plainhtml.extract_text(html)
'foo\n\nbar'
```
