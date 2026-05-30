## 2024-05-30 - Path Traversal in Filename Sanitization
**Vulnerability:** The `sanitize_filename` function only removed specific characters `[\\/*?:"<>|]`, but failed to handle path traversal sequences like `..` or leading dots. A malicious project or item title could lead to files being written outside the intended export directory.
**Learning:** Simple blacklisting of characters is often insufficient for file system operations. `..` is a valid sequence of characters that can still cause path traversal if not explicitly handled or if the resulting path is not validated.
**Prevention:** Always strip leading dots and collapse/remove sequences of dots in user-provided strings used for filenames. Providing a fallback for empty strings after sanitization is also crucial.
