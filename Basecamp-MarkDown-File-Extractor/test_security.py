import re
import unittest
from pathlib import Path
import sys
import os

# Import the function to be tested
sys.path.append(os.path.dirname(__file__))

class TestSecurity(unittest.TestCase):
    def setUp(self):
        try:
            from extractor import sanitize_filename as sanitize_bc2
            from extractor_bc3 import sanitize_filename as sanitize_bc3
            self.sanitize_bc2 = sanitize_bc2
            self.sanitize_bc3 = sanitize_bc3
        except ImportError as e:
            self.fail(f"Could not import sanitize_filename: {e}")

    def _test_implementation(self, sanitize_func):
        payloads = [
            "..",
            "../",
            "../../etc/passwd",
            "C:\\Windows\\System32\\config\\SAM",
            ".ssh/authorized_keys",
            "../../../secret.txt"
        ]
        for payload in payloads:
            sanitized = sanitize_func(payload)
            self.assertNotIn("..", sanitized, f"Failed for payload: {payload}")
            self.assertNotIn("/", sanitized, f"Failed for payload: {payload}")
            self.assertNotIn("\\", sanitized, f"Failed for payload: {payload}")

            # Ensure it doesn't resolve to something outside a base directory
            # We use a dummy base directory for testing resolution
            base = Path("/app/exports").resolve()
            # If sanitized is empty or just dots, Path(base / sanitized).resolve() might still go up.
            # But we want to ensure 'sanitized' itself is safe.
            target = (base / sanitized).resolve()
            self.assertTrue(str(target).startswith(str(base)), f"Payload '{payload}' (sanitized to '{sanitized}') escaped base directory!")

    def test_bc2_implementation(self):
        self._test_implementation(self.sanitize_bc2)

    def test_bc3_implementation(self):
        self._test_implementation(self.sanitize_bc3)

    def test_empty_fallback(self):
        for func in [self.sanitize_bc2, self.sanitize_bc3]:
            payloads = ["", " ", "...", "/", "\\"]
            for payload in payloads:
                sanitized = func(payload)
                self.assertTrue(len(sanitized) > 0, f"Function {func.__module__} returned empty string for payload '{payload}'")
                self.assertNotEqual(sanitized, ".", f"Function {func.__module__} returned '.' for payload '{payload}'")
                self.assertNotEqual(sanitized, "..", f"Function {func.__module__} returned '..' for payload '{payload}'")

if __name__ == "__main__":
    unittest.main()
