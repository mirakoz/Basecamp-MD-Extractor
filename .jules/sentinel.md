## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-15 - HTML Metadata Leakage and XSS in Exports
**Vulnerability:** The HTML cleaning functions were only removing UI-specific classes (like `.button`, `.admin`), leaving sensitive `<meta>` tags (containing CSRF tokens) and `<script>` tags intact in the Markdown output.
**Learning:** When extracting content from web pages, especially with a fallback to `page.content()`, relying solely on UI-specific selectors is insufficient. Secure extraction requires explicitly stripping high-risk tags that could leak internal state or execute scripts.
**Prevention:** The `clean_html` function must explicitly decompose `script`, `style`, `meta`, and `link` tags before processing the content for Markdown conversion.
