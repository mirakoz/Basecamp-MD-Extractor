## 2025-05-21 - Path Traversal in Filename Sanitization
**Vulnerability:** The `sanitize_filename` function only removed specific characters but allowed relative path components like `.` and `..`. Combined with `Path` joining, this allowed writing files outside the intended export directory.
**Learning:** Simple character blacklisting is insufficient for filename sanitization. Trailing/leading dots and spaces can be used for traversal or creating hidden files on Unix-like systems.
**Prevention:** Use a whitelist-based approach or aggressively strip leading/trailing dots and spaces. Always provide a safe fallback for empty strings resulting from sanitization.
