import unittest
import sys
import os

# Add the directory to sys.path to import from extractor
sys.path.append(os.path.dirname(__file__))

try:
    from extractor import sanitize_filename
except ImportError:
    from Basecamp_MarkDown_File_Extractor.extractor import sanitize_filename


class TestSecurity(unittest.TestCase):
    def test_sanitize_filename(self):
        test_cases = [
            ("normal_file", "normal_file"),
            ("file/with/slashes", "filewithslashes"),
            ("../../etc/passwd", "etcpasswd"),
            ("..", "unnamed"),
            (".", "unnamed"),
            ("   ", "unnamed"),
            ("", "unnamed"),
            ("dots...dots", "dots.dots"),
            (".leading_dot", "leading_dot"),
            ("trailing_dot.", "trailing_dot."),
            ("?invalid*", "invalid"),
        ]

        for input_name, expected in test_cases:
            with self.subTest(input_name=input_name):
                self.assertEqual(sanitize_filename(input_name), expected)


if __name__ == "__main__":
    unittest.main()
