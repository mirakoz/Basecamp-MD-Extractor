## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Sensitive Data Exposure in Exported Markdown
**Vulnerability:** The HTML cleaning functions were relying on UI-specific class selectors, allowing sensitive metadata (like CSRF tokens in `<meta>` tags), internal styles, and potentially malicious scripts to be included in the exported Markdown files.
**Learning:** When scraping web content, using `page.content()` as a fallback or even targeting specific containers can leak sensitive page metadata if the cleaning logic is not exhaustive. Explicitly stripping non-content tags like `meta`, `script`, and `style` is a mandatory security baseline.
**Prevention:** Always explicitly decompose `script`, `style`, `meta`, `link`, and `form` tags in HTML sanitization functions before converting to Markdown.
