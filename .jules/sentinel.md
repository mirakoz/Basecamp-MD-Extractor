## 2025-05-15 - [CRITICAL] Fix Path Traversal in Filename Sanitization
**Vulnerability:** The `sanitize_filename` function only removed a limited set of characters and didn't strip leading/trailing dots or spaces, allowing path traversal (e.g., using `..` as a title) and the creation of hidden files.
**Learning:** Simple regex-based character removal is insufficient for filename sanitization if it doesn't account for filesystem-specific meanings of `.` and `..` or leading/trailing whitespace.
**Prevention:** Always strip leading and trailing dots and spaces from user-provided filenames, and ensure the resulting string is not empty by providing a secure fallback.
