**Pytest uchun test kod**
```python
import pytest
from unittest.mock import patch
from your_module import clean_text

@pytest.mark.parametrize("text, expected", [
    ("   Hello World   ", "Hello World"),
    ("  This is a test  ", "This is a test"),
    ("   ", ""),
])
def test_clean_text(text, expected):
    with patch('builtins.print') as mock_print:
        clean_text(text)
        assert mock_print.call_count == 0
        assert clean_text(text) == expected

def test_clean_text_empty_string():
    assert clean_text("") == ""

def test_clean_text_no_spaces():
    assert clean_text("HelloWorld") == "HelloWorld"
```

**Jest uchun test kod**
```javascript
describe('cleanText', () => {
  it('should remove leading and trailing spaces', () => {
    const text = '   Hello World   ';
    const expected = 'Hello World';
    expect(cleanText(text)).toBe(expected);
  });

  it('should remove leading and trailing spaces from empty string', () => {
    const text = '';
    const expected = '';
    expect(cleanText(text)).toBe(expected);
  });

  it('should not remove spaces from string without spaces', () => {
    const text = 'HelloWorld';
    const expected = 'HelloWorld';
    expect(cleanText(text)).toBe(expected);
  });
});
```
