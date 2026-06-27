## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-05-16 - Sensitive Data Exposure in Sample Files and Insufficient HTML Cleaning
**Vulnerability:** Sample HTML files containing PII, project data, and CSRF tokens were committed to the repository. Additionally, HTML cleaning functions only targeted UI elements, potentially leaving scripts and metadata in the exported Markdown.
**Learning:** Sample files for testing/debugging can easily leak sensitive production data if not properly sanitized or excluded from the repository. Relying on specific UI class selectors for cleaning is insufficient; a robust approach should also target potentially dangerous or sensitive tags like `script` and `meta`.
**Prevention:** Never commit files containing production data or session tokens. Use synthetic data for samples. Harden HTML cleaning by explicitly decomposing `script`, `style`, `meta`, `link`, and `form` tags to ensure exported content is clean and safe.
