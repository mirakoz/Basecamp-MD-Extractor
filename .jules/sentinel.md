## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-15 - Sensitive Data Leakage in HTML Extraction
**Vulnerability:** Extraction scripts (`extractor.py`, `extractor_bc3.py`) were not stripping `meta`, `script`, `style`, and `link` tags from the HTML before converting to Markdown. This leaked sensitive information like CSRF tokens and internal metadata into the exported files.
**Learning:** Cleaning only UI elements (buttons, forms) is insufficient when exporting web content to persistent files. Metadata tags often contain session-specific or sensitive security tokens.
**Prevention:** Explicitly remove all non-content tags like `script`, `style`, `meta`, and `link` during the HTML cleaning phase of data extraction.
