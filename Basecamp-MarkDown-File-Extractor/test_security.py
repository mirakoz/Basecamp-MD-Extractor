import unittest
import re
from extractor import sanitize_filename

class TestSecurity(unittest.TestCase):
    def test_sanitize_filename_path_traversal(self):
        # Test cases for path traversal
        self.assertEqual(sanitize_filename("../etc/passwd"), "etcpasswd")
        self.assertEqual(sanitize_filename("../../hidden"), "hidden")
        self.assertEqual(sanitize_filename("..\\..\\win.ini"), "win.ini")

    def test_sanitize_filename_leading_dots(self):
        # Test cases for leading dots (hidden files)
        self.assertEqual(sanitize_filename(".env"), "env")
        self.assertEqual(sanitize_filename(".ssh/id_rsa"), "sshid_rsa")

    def test_sanitize_filename_multiple_dots(self):
        # Test cases for multiple dots
        self.assertEqual(sanitize_filename("file...txt"), "file.txt")
        self.assertEqual(sanitize_filename("my..name"), "my.name")

    def test_sanitize_filename_invalid_chars(self):
        # Test cases for invalid characters
        self.assertEqual(sanitize_filename("hello/world"), "helloworld")
        self.assertEqual(sanitize_filename("a*b?c:d"), "abcd")
        self.assertEqual(sanitize_filename("title <script>"), "title script")

    def test_sanitize_filename_strip(self):
        # Test case for stripping whitespace
        self.assertEqual(sanitize_filename("  my file  "), "my file")

if __name__ == '__main__':
    unittest.main()
