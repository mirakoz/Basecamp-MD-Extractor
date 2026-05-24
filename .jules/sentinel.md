## 2025-05-15 - Path Traversal Vulnerability in Filename Sanitization
**Vulnerability:** The `sanitize_filename` function only removed specific characters `[\\/*?:"<>|]` but did not handle leading dots or multiple dots. This could allow for path traversal (e.g., using `..`) or the creation of hidden files (e.g., `.bashrc`) when exporting Basecamp content to Markdown files.
**Learning:** Simple blacklisting of characters is often insufficient for filename sanitization. Security-sensitive filename generation must also consider special path components and hidden file conventions.
**Prevention:** Always strip leading dots, collapse multiple dots, and ensure the resulting filename is not empty by providing a default value.
