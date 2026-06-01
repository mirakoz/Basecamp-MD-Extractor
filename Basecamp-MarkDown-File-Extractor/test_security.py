import re
import unittest

# Importing the implementation from extractor.py would be ideal,
# but for the sake of the initial test we'll use the one we found.
def sanitize_filename_vulnerable(name):
    # Current implementation in extractor.py
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

class TestSecurity(unittest.TestCase):
    def test_sanitize_filename_security(self):
        # These are the cases we WANT to pass after fixing
        cases = [
            ("../../etc/passwd", "etcpasswd"),
            ("..", "unnamed"),
            (".", "unnamed"),
            (".ssh", "ssh"),
            ("normal_file", "normal_file"),
            ("", "unnamed"),
            ("   ", "unnamed"),
            ("file.with.dots", "filewithdots"), # Simplest approach: remove all dots
        ]

        # Note: The current implementation will FAIL many of these.
        # We will use the 'vulnerable' version here just to demonstrate failure in the thought process,
        # but the actual test file should eventually test the 'real' function.

        from extractor import sanitize_filename

        for input_name, expected in cases:
            with self.subTest(input_name=input_name):
                actual = sanitize_filename(input_name)
                self.assertEqual(actual, expected, f"Failed for input: {input_name}")

if __name__ == "__main__":
    unittest.main()
