import unittest
import re
from pathlib import Path


def sanitize_filename(name):
    # The updated implementation
    sanitized = re.sub(r'[\\/*?:"<>|.]', "", name).strip()
    return sanitized if sanitized else "unnamed"


class TestSecurity(unittest.TestCase):
    def test_path_traversal(self):
        payloads = [
            "../../etc/passwd",
            "..\\..\\windows\\system32\\config\\sam",
            "../../../secret",
            ".ssh/authorized_keys",
            "C:\\Users\\Admin\\AppData\\Local\\Temp",
            "/absolute/path",
            "dot.dot",
            "...",
            "   ",
            "",
            "normal_title",
            "Title with / slash",
        ]

        base_dir = Path("/tmp/base_exports")

        for payload in payloads:
            sanitized = sanitize_filename(payload)
            target_path = base_dir / sanitized

            # Verify that the sanitized name does not contain dots or separators
            self.assertNotIn("..", sanitized)
            self.assertNotIn("/", sanitized)
            self.assertNotIn("\\", sanitized)
            self.assertNotIn(".", sanitized)
            self.assertTrue(len(sanitized) > 0)

            # Verify that the path is strictly within the base directory
            # (In this case, since we remove all dots and separators, it's guaranteed to be a single filename)
            self.assertEqual(target_path.parent, base_dir)

            print(
                f"Payload: {payload:40} -> Sanitized: {sanitized:20} -> Path: {target_path}"
            )


if __name__ == "__main__":
    unittest.main()
