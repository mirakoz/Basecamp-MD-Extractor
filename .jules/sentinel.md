## 2026-05-26 - [Path Traversal in Filename Sanitization]
**Vulnerability:** The `sanitize_filename` function was only removing a specific set of invalid characters `[\\/*?:"<>|]`, but it allowed filenames like `..`. When these sanitized names were used with `pathlib.Path` to create directories or files (e.g., `EXPORTS_DIR / project_title`), it allowed for directory traversal, potentially writing files outside of the intended export directory.

**Learning:** Relying solely on character blacklisting for filename sanitization is insufficient to prevent path traversal. `pathlib` correctly handles `..` as a parent directory reference, which can be exploited if the input is not properly cleaned of path-navigation components.

**Prevention:** Filename sanitization should also include stripping leading dots, collapsing multiple dots, and ensuring the resulting name is not empty or a reserved name. Using a whitelist of allowed characters is generally safer than a blacklist.
