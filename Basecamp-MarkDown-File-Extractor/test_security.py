import unittest
from extractor import sanitize_filename as sanitize_bc2
from extractor_bc3 import sanitize_filename as sanitize_bc3

class TestSecurity(unittest.TestCase):
    def test_path_traversal(self):
        for sanitize in [sanitize_bc2, sanitize_bc3]:
            # Test that .. is removed from start or collapsed
            self.assertEqual(sanitize(".."), "unnamed")
            self.assertEqual(sanitize("../../etc/passwd"), "etcpasswd")
            self.assertEqual(sanitize("some..name"), "some.name")
            self.assertEqual(sanitize("...dots"), "dots")

    def test_invalid_chars(self):
        for sanitize in [sanitize_bc2, sanitize_bc3]:
            self.assertEqual(sanitize("file*name?"), "filename")
            self.assertEqual(sanitize("file:name"), "filename")

    def test_empty_result(self):
        for sanitize in [sanitize_bc2, sanitize_bc3]:
            self.assertEqual(sanitize("*?:"), "unnamed")

    def test_hidden_files(self):
        for sanitize in [sanitize_bc2, sanitize_bc3]:
            # Leading dots should be removed to avoid creating hidden files
            self.assertEqual(sanitize(".bashrc"), "bashrc")

if __name__ == "__main__":
    unittest.main()
