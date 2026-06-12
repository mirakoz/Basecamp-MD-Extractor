## 2025-05-14 - Fix Path Traversal in Filename Sanitization
**Vulnerability:** The `sanitize_filename` function only removed specific characters but didn't handle special filenames like ".." or leading/trailing dots/spaces, which could lead to path traversal or creation of hidden files.
**Learning:** Even simple character removal isn't enough for safe filename generation; special filesystem reserved names and dot-prefixed hidden files must be considered.
**Prevention:** Always strip leading/trailing dots and spaces from sanitized filenames and provide a fallback ("unnamed") if the result is empty.
