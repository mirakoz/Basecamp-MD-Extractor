## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Sensitive Data Exposure in Sample Artifacts
**Vulnerability:** Several sample HTML files were checked into the repository containing PII, business data, and plaintext administrative credentials.
**Learning:** Development artifacts, debug files, or "sample" data can often contain sensitive information if not carefully audited before commit. Extraction tools that use `page.content()` as a fallback can capture sensitive metadata (scripts, tokens, etc.) that isn't visible in the UI.
**Prevention:** Never commit raw HTML dumps from production systems to the repository. Harden extraction logic to explicitly strip sensitive tags (`script`, `style`, `meta`, `link`, `form`) even when falling back to full page content.
