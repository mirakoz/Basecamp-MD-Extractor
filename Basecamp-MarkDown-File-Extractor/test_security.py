import unittest
import re
import os
from pathlib import Path

# Import sanitize_filename from extractor
# We use a trick to import it since it's in the same directory but we might run from root
try:
    from extractor import sanitize_filename
except ImportError:
    import sys

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from extractor import sanitize_filename


class TestSecurity(unittest.TestCase):
    def test_path_traversal_dots(self):
        """Test that '..' is sanitized to prevent path traversal."""
        unsafe_name = ".."
        sanitized = sanitize_filename(unsafe_name)

        # Current implementation returns '..' which is dangerous
        # Improved implementation should return something else or empty string (which might need handling)
        # or it should be handled such that it doesn't resolve to parent directory.

        self.assertNotEqual(
            sanitized, "..", f"Vulnerability: '{unsafe_name}' was not sanitized!"
        )
        self.assertNotEqual(
            sanitized, ".", f"Vulnerability: '{unsafe_name}' was sanitized to '.'!"
        )

    def test_path_traversal_leading_dots(self):
        """Test that leading dots are removed."""
        unsafe_name = "../secret"
        sanitized = sanitize_filename(unsafe_name)
        self.assertFalse(
            sanitized.startswith(".."),
            f"Vulnerability: '{unsafe_name}' still starts with '..'!",
        )

    def test_invalid_characters(self):
        """Ensure existing sanitization still works."""
        name = 'test/\\*?:"<>|file'
        sanitized = sanitize_filename(name)
        for char in '[\\/*?:"<>|]':
            self.assertNotIn(char, sanitized)


if __name__ == "__main__":
    unittest.main()
