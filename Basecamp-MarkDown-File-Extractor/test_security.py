import sys
import os

# Add the directory to sys.path to import from it
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extractor import sanitize_filename as sanitize_bc2
from extractor_bc3 import sanitize_filename as sanitize_bc3

def test():
    test_cases = [
        ("Normal Title", "Normal Title"),
        ("Title / with / slashes", "Title  with  slashes"),
        ("..", ""),
        ("../../../etc/passwd", "etcpasswd"),
        (".hidden", "hidden"),
        ("file...name", "file.name"),
        ("  ..  ", ""), # Leading/trailing whitespace
        ("  .hidden", "hidden")
    ]

    all_passed = True

    print("Testing extractor.py sanitize_filename:")
    for input_val, expected in test_cases:
        actual = sanitize_bc2(input_val)
        status = "PASS" if actual == expected else "FAIL"
        print(f"  '{input_val}' -> '{actual}' (expected '{expected}') - {status}")
        if status == "FAIL":
            all_passed = False

    print("\nTesting extractor_bc3.py sanitize_filename:")
    for input_val, expected in test_cases:
        actual = sanitize_bc3(input_val)
        status = "PASS" if actual == expected else "FAIL"
        print(f"  '{input_val}' -> '{actual}' (expected '{expected}') - {status}")
        if status == "FAIL":
            all_passed = False

    if all_passed:
        print("\nBoth implementations passed all security tests.")
    else:
        print("\nSome tests FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    test()
