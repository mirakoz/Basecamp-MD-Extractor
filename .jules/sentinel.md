## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Sensitive Data Exposure in Sample Files
**Vulnerability:** Sample HTML files and sync scripts contained PII (email, names), CSRF tokens, and hardcoded absolute paths revealing local user home directories.
**Learning:** Hardcoded sample data used for testing can easily leak sensitive information if not properly scrubbed or excluded from the repository. Fallback mechanisms in extractors (like `page.content()`) can also capture sensitive metadata if cleaning is not thorough.
**Prevention:** Avoid committing real-world HTML samples. Harden `clean_html` functions to explicitly strip `script`, `style`, `meta`, and `link` tags. Use dynamic path determination in scripts.
