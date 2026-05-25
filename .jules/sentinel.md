## 2025-05-15 - [Path Traversal in Filename Sanitization]
**Vulnerability:** Insufficient filename sanitization allowed for potential path traversal and creation of hidden files (e.g., `.env`) when exporting Basecamp content. The original `sanitize_filename` only removed common illegal characters but didn't handle leading dots or multiple dots.
**Learning:** Even simple character-based filtering for filenames can be bypassed by using dots to navigate directories or create hidden system files.
**Prevention:** Always strip leading dots and collapse multiple dots in user-influenced filenames to ensure they stay within the intended directory and are visible.
