## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** The `sanitize_filename` function only removed specific characters (`[\\/*?:"<>|]`) and stripped whitespace, which allowed path traversal components like `..` or hidden file markers (leading `.`) to persist if they were part of a project title.
**Learning:** Insecure filename sanitization that doesn't account for filesystem navigation sequences can lead to arbitrary file write vulnerabilities even when "illegal" characters are removed.
**Prevention:** Always strip leading and trailing dots and spaces from filenames, and provide a safe fallback (e.g., 'unnamed') if the resulting string is empty or invalid.
