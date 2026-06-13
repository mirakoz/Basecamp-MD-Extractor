## 2025-05-14 - Path Traversal in Filename Sanitization
**Vulnerability:** Weak filename sanitization allowed for path traversal (e.g., via "..") and the creation of hidden files (e.g., via ".hidden") by not stripping leading/trailing dots and spaces.
**Learning:** Using `strip()` or `strip(". ")` is crucial after removing illegal characters to prevent attackers from using relative path segments that remain valid filenames but cause traversal when joined with a base directory.
**Prevention:** Always strip leading and trailing dots and spaces from user-provided strings intended for filenames, and provide a non-empty fallback if the resulting string is empty.
