## 2024-05-23 - Path Traversal in Filename Sanitization
**Vulnerability:** Path traversal and hidden file creation via malicious project or message titles.
**Learning:** The original `sanitize_filename` function only removed specific characters but allowed dots (`.`), which could be used to create files named `..` or `.hidden`, potentially causing issues on some filesystems or hiding exported data.
**Prevention:** Always strip all dots from filenames derived from external input if they are not strictly necessary, and provide a non-empty fallback string to ensure file creation always succeeds.
