## 2026-05-23 - [Path Traversal in Filename Sanitization]
**Vulnerability:** Filenames generated from Basecamp project or message titles were sanitized only for invalid characters (like `/`, `*`, `?`), but did not account for path traversal sequences like `..` or leading dots. This could allow an attacker to write files outside the intended export directory.
**Learning:** Simple regex-based character replacement is insufficient for filename sanitization if it doesn't also handle path-relative sequences.
**Prevention:** Always strip leading dots, collapse multiple dots, and ensure the resulting filename does not result in a path traversal sequence.
