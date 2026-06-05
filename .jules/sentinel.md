## 2025-06-05 - 🛡️ Sentinel: [HIGH] Fix path traversal in filename sanitization
**Vulnerability:** Path traversal via filename injection. The `sanitize_filename` function only removed specific characters `[\\/*?:"<>|]`, allowing `..` and `.` which could lead to files being written outside the intended export directory.
**Learning:** Sanitization must account for relative path markers like `..` and `.`, especially when user-controlled strings (like project or message titles) are used to construct file paths.
**Prevention:** Remove all dots from filenames when they are not strictly necessary for functionality, and ensure a fallback name is provided if sanitization results in an empty string.
