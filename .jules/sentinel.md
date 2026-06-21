## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - XSS Risk in HTML Extraction
**Vulnerability:** The HTML cleaning functions (`clean_html` and `clean_html_bc3`) failed to explicitly strip `script`, `style`, `meta`, and `link` tags.
**Learning:** Relying on UI-specific class selectors to clean HTML is insufficient for security; generic dangerous tags must be explicitly decomposed to prevent XSS and information leakage.
**Prevention:** Always include `script`, `style`, `meta`, and `link` in the list of selectors to be decomposed during HTML sanitization.
