import os
import sys

# Add the directory to sys.path so we can import from extractor
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extractor import sanitize_filename as sanitize_bc2
from extractor_bc3 import sanitize_filename as sanitize_bc3

def test_sanitize_filename():
    test_cases = [
        ("Normal Title", "Normal Title"),
        ("Title / with / Slashes", "Title  with  Slashes"),
        ("../../etc/passwd", "etcpasswd"),
        ("..", "unnamed"),
        ("...", "unnamed"),
        (".hidden", "hidden"),
        ("Title with \"quotes\"", "Title with quotes"),
        ("", "unnamed"),
    ]

    for name, sanitize_func in [("BC2", sanitize_bc2), ("BC3", sanitize_bc3)]:
        print(f"Testing {name} sanitize_filename implementation...")
        all_passed = True
        for input_name, expected in test_cases:
            actual = sanitize_func(input_name)
            if actual != expected:
                print(f"FAIL: '{input_name}' -> expected '{expected}', got '{actual}'")
                all_passed = False
            else:
                print(f"PASS: '{input_name}' -> '{actual}'")

        # Explicit security checks for path traversal
        security_cases = ["..", "../..", "..\\..", ".", "./"]
        for sc in security_cases:
            sanitized = sanitize_func(sc)
            if sanitized in [".", ".."] or sanitized == "":
                 print(f"SECURITY ALERT: '{sc}' sanitized to '{sanitized}' which is dangerous!")
                 all_passed = False

        if all_passed:
            print(f"All {name} tests passed!")
        else:
            print(f"Some {name} tests failed.")
            exit(1)

if __name__ == "__main__":
    test_sanitize_filename()
