## 2025-05-15 - Prevent Path Traversal in Filename Sanitization
**Vulnerability:** The `sanitize_filename` function only removed a small set of characters (`[\\/*?:"<>|]`), which allowed path traversal sequences like `..` and hidden files starting with `.` to persist.
**Learning:** Generic filename sanitization must account for filesystem-level control characters, especially dot sequences, which can be used to navigate outside the intended export directory.
**Prevention:** Remove all dot sequences and separators, and ensure a fallback filename is provided if sanitization results in an empty string.
