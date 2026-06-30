## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Sensitive Data Exposure in Sample HTML Files
**Vulnerability:** Several sample HTML files in the repository contained sensitive project data, PII (email addresses), and active CSRF tokens from Basecamp sessions.
**Learning:** Checking in raw HTML saved from a browser can accidentally leak credentials and sensitive information if not thoroughly cleaned. These files also posed a risk if the extraction scripts fell back to `page.content()`, as the hardened `clean_html` logic was not previously applied to all sensitive tags like `<meta>` or `<link>`.
**Prevention:** Never commit raw browser-saved HTML files. If sample data is needed, use synthetic or thoroughly anonymized data. Robust HTML cleaning must be mandatory for any tool that processes web content to prevent accidental leakage of sensitive page metadata.
