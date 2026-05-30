import re
import unittest
from pathlib import Path

# Since we want to test the function in the context of the extractors
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from extractor import sanitize_filename as sanitize_bc2
from extractor_bc3 import sanitize_filename as sanitize_bc3

class TestSecurity(unittest.TestCase):
    def test_sanitize_filename_path_traversal(self):
        cases = [
            ("..", "unnamed"),
            ("../../etc/passwd", "etcpasswd"),
            ("project/../secret", "projectsecret"),
            (".hidden", "hidden"),
            ("...", "unnamed"),
            ("   ", "unnamed"),
            ("", "unnamed"),
        ]

        for input_name, expected in cases:
            with self.subTest(input_name=input_name):
                # Testing BC2
                result_bc2 = sanitize_bc2(input_name)
                # Testing BC3
                result_bc3 = sanitize_bc3(input_name)

                self.assertEqual(result_bc2, expected, f"BC2 failed for {input_name}")
                self.assertEqual(result_bc3, expected, f"BC3 failed for {input_name}")

    def test_sanitize_filename_invalid_chars(self):
        cases = [
            ('file*name?', 'filename'),
            ('lpt1', 'lpt1'), # Basic sanitization doesn't usually handle reserved names unless specified
            ('valid-name_123', 'valid-name_123'),
        ]
        for input_name, expected in cases:
            with self.subTest(input_name=input_name):
                self.assertEqual(sanitize_bc2(input_name), expected)
                self.assertEqual(sanitize_bc3(input_name), expected)

if __name__ == "__main__":
    unittest.main()
