import unittest
from extractor import sanitize_filename

class TestSecurity(unittest.TestCase):
    def test_sanitize_filename_path_traversal(self):
        test_cases = [
            ("..", ""),
            ("../..", ""),
            ("foo/bar", "foobar"),
            ("..\\..\\etc\\passwd", "etcpasswd"),
            (".../secret", "secret"),
            (".hidden", "hidden"),
            ("normal_file.txt", "normal_file.txt"),
            ("file with spaces.md", "file with spaces.md"),
            ("invalid<>|:\"*?\\char.txt", "invalidchar.txt"),
            ("./././config.yml", "config.yml"),
        ]

        for input_name, expected in test_cases:
            with self.subTest(input_name=input_name):
                sanitized = sanitize_filename(input_name)
                self.assertEqual(sanitized, expected, f"Failed for {input_name}")

if __name__ == "__main__":
    unittest.main()
