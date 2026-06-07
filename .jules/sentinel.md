## 2025-05-14 - Fix Path Traversal in Filename Sanitization
**Vulnerability:** Path traversal via dots in filenames.
**Learning:** The initial `sanitize_filename` function only removed characters like `/` and `\`, but allowed `..`, which enabled writing files outside the intended export directory.
**Prevention:** Use a more restrictive sanitization pattern that removes all dots and provides a fallback name if the sanitized result is empty.
