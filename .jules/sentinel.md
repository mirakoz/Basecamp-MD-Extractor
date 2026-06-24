## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Sensitive Data Exposure in Sample HTML and Incomplete Cleaning
**Vulnerability:** Sample HTML files contained hardcoded credentials, PII, and sensitive corporate data. Additionally, HTML cleaning functions failed to strip `script`, `meta`, `style`, and `link` tags.
**Learning:** Sample data used for development/testing often contains real, sensitive production data if not carefully sanitized. Relying solely on class-based selectors for cleaning is insufficient when capturing full page content.
**Prevention:** Never commit raw HTML dumps from production to a repository. Always explicitly strip sensitive metadata tags (`script`, `meta`, `style`, `link`, `form`) when scraping web pages to ensure defense-in-depth against accidental leakage.
