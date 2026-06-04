## 2026-06-04 - Fix path traversal in filename sanitization
**Vulnerability:** The `sanitize_filename` function only removed specific characters `[\\/*?:"<>|]`, allowing `..` sequences to remain. This could lead to path traversal vulnerabilities where exported files are written outside the intended directory.
**Learning:** Blacklisting a small set of characters is often insufficient for security-critical operations like filename sanitization. Traversal sequences like `..` must be explicitly handled.
**Prevention:** Update `sanitize_filename` to remove all dots and ensure the resulting filename is not empty by providing a fallback.
