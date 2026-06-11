## 2025-05-15 - Fix path traversal in filename sanitization
**Vulnerability:** Path traversal in the `sanitize_filename` function. By using ".." as a project or message title, an attacker could potentially cause the extractor to write files outside of the designated export directory.
**Learning:** Simply stripping invalid characters and using a generic `.strip()` is insufficient for filename sanitization. Specifically, ".." must be prevented as it can be used to navigate to parent directories.
**Prevention:** Always strip leading and trailing dots and spaces from filenames, and ensure a fallback name is provided if the resulting string becomes empty.
