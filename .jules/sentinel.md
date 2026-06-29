## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Exposure of Sensitive Data in Sample HTML Files
**Vulnerability:** Committed HTML files in the `Basecamp-MarkDown-File-Extractor/` directory contained CSRF tokens, PII (names/emails), and private project data.
**Learning:** Sample or debug data files can easily leak sensitive information if they are generated from a live account and committed to the repository.
**Prevention:** Never commit HTML snapshots or debug logs generated from live sessions; add them to `.gitignore` and use synthetic data for testing. Robustly clean HTML in the extractor to prevent accidental leakage from metadata.
