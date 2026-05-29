## 2025-05-15 - Path Traversal via Filename Sanitization
**Vulnerability:** Path traversal vulnerabilities allowed attackers to escape the intended export directory by using filenames like `../../etc/passwd` or `..`.
**Learning:** Simple character-based blacklisting (removing `\/*?:"<>|`) is insufficient to prevent path traversal when the resulting string can still contain leading dots or be empty.
**Prevention:** Always strip leading dots and spaces from filenames, collapse multiple dots, and provide a safe fallback for empty or completely sanitized strings.
