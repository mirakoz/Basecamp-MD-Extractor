## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** The `sanitize_filename` function only removed a limited set of characters (`[\\/*?:"<>|]`), allowing dots (`.`) to remain. This enabled path traversal attacks (e.g., using `..`) and the creation of hidden files (e.g., `.ssh`).
**Learning:** Simple blacklists for filename sanitization are often insufficient. In many file systems, dots are special and must be handled to prevent directory traversal.
**Prevention:** Use a more robust sanitization approach that removes all dots or specifically blocks traversal sequences. Always provide a fallback name if sanitization results in an empty string to prevent issues with path construction.
