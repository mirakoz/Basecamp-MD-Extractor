## 2025-05-15 - Privacy risk in sync configuration
**Vulnerability:** Hardcoded absolute paths in `run_sync.sh` and `com.basecamp.sync.plist`.
**Learning:** Hardcoded absolute paths to a specific user's home directory (`/Users/mirakozoglu/...`) leak information about the developer's environment and make the scripts non-portable.
**Prevention:** Use dynamic path lookups in scripts (e.g., `$(dirname "$0")` in bash) to avoid hardcoding local system structure.

## 2025-05-15 - Path traversal in filename sanitization
**Vulnerability:** Weak filename sanitization allowing leading dots and empty strings.
**Learning:** Only removing a subset of filesystem special characters while allowing leading dots (`.`) can lead to hidden files or traversal attempts if combined with other issues. However, stripping all dots causes functional regressions for titles with decimals.
**Prevention:** Filename sanitization should remove leading/trailing dots and invalid characters, while providing a safe fallback name if the result is empty.
