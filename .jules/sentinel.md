## 2025-05-15 - Path Traversal in Filename Sanitization
**Vulnerability:** Insufficient filename sanitization in `extractor.py` and `extractor_bc3.py` allowed path traversal via `..` and creation of hidden files via leading dots.
**Learning:** Simply removing common illegal characters like `/` or `\` is not enough if the resulting string can still be `..` or start with a dot, which can lead to files being written outside the intended directory or being hidden.
**Prevention:** Always strip leading and trailing dots and spaces from filenames after removing illegal characters, and provide a fallback name if the resulting string is empty.

## 2026-06-22 - Information Leakage and XSS in HTML Exports
**Vulnerability:** HTML extraction scripts for Basecamp 2 and 3 did not strip sensitive tags like `<script>`, `<style>`, `<meta>`, and `<link>` before converting to Markdown.
**Learning:** Relying solely on UI-specific class selectors for cleaning HTML is insufficient when the page contains sensitive metadata (like `csrf-token` or `dropbox_key`) in non-UI tags. If content selectors fail, the script falls back to the full page content, making this particularly dangerous.
**Prevention:** Explicitly decompose all potentially dangerous or sensitive tags (`script`, `style`, `meta`, `link`, `form`) in the HTML cleaning phase to ensure a clean and secure export.
