## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Sensitive Data Exposure in Sample HTML
**Vulnerability:** Sample HTML files (e.g., `todos.html`, `bc3_messages.html`) were committed to the repository containing real-world PII (emails, names) and active CSRF tokens.
**Learning:** Automated extraction scripts that fall back to `page.content()` when selectors fail can accidentally leak sensitive page metadata if the cleaning logic is not comprehensive.
**Prevention:** Hardened HTML cleaning functions must explicitly decompose `script`, `style`, `meta`, `link`, and `form` tags. Ensure sample artifacts are sanitized or removed before committing.
