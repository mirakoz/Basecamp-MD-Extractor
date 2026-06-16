## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2025-06-16 - Information Leakage in HTML Extraction
**Vulnerability:** Incomplete HTML sanitization allowed sensitive tags like `<meta>` (containing CSRF tokens), `<script>`, and `<style>` to be preserved in exported Markdown.
**Learning:** When extracting content from a live web application for static export, common UI-stripping is insufficient; structural and sensitive metadata tags must be explicitly removed to prevent session data leakage and XSS.
**Prevention:** Ensure all extraction cleaning functions maintain a denylist of tags that include `script`, `style`, `meta`, and `link`.
