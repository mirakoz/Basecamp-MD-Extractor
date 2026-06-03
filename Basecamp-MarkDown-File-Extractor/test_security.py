import unittest
from extractor import sanitize_filename

class TestSanitizeFilename(unittest.TestCase):
    def test_basic_sanitization(self):
        self.assertEqual(sanitize_filename("Normal Title"), "Normal Title")
        self.assertEqual(sanitize_filename("Title / With \\ Slashes"), "Title  With  Slashes")

    def test_path_traversal_prevention(self):
        # Dots should be removed to prevent traversal
        self.assertEqual(sanitize_filename(".."), "unnamed")
        self.assertEqual(sanitize_filename("../../../etc/passwd"), "etcpasswd")
        self.assertEqual(sanitize_filename("file.txt"), "filetxt")
        self.assertEqual(sanitize_filename("..."), "unnamed")

    def test_invalid_characters(self):
        self.assertEqual(sanitize_filename('invalid:*?"<>|'), "invalid")

    def test_empty_result_fallback(self):
        self.assertEqual(sanitize_filename(""), "unnamed")
        self.assertEqual(sanitize_filename('   '), "unnamed")
        self.assertEqual(sanitize_filename('...///:::'), "unnamed")

if __name__ == '__main__':
    unittest.main()
