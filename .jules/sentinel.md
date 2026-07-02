## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Sensitive Data Exposure in Committed HTML Files
**Vulnerability:** Committed sample HTML files contained PII, CSRF tokens, and administrative credentials in plaintext.
**Learning:** Sample files captured during development often leak sensitive production data. Relying solely on UI-specific selectors for HTML cleaning is insufficient when scripts fall back to full page content.
**Prevention:** Remove all sensitive HTML files from the repository. Harden HTML cleaning functions to explicitly strip `script`, `style`, `meta`, `link`, and `form` tags to prevent metadata and script leakage.
