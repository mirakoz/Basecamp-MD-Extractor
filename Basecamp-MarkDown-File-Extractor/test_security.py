import sys
import os

# Add the directory to sys.path to import the extractors
sys.path.append(os.path.join(os.getcwd(), "Basecamp-MarkDown-File-Extractor"))

try:
    from extractor import sanitize_filename as sanitize_bc2
    from extractor_bc3 import sanitize_filename as sanitize_bc3
except ImportError as e:
    print(f"ImportError: {e}")
    sys.exit(1)

def test_sanitize():
    test_cases = [
        ("Normal Title", "Normal Title"),
        ("Title with / slash", "Title with  slash"),
        ("Title with : colon", "Title with  colon"),
        ("..", "unnamed"),
        ("../relative/path", "relativepath"),
        (".../secret.txt", "secrettxt"),
    ]

    print("Testing BC2 sanitize_filename...")
    for input_name, expected in test_cases:
        actual = sanitize_bc2(input_name)
        print(f"  Input: '{input_name}' -> Actual: '{actual}' (Expected: '{expected}')")
        assert actual == expected

    print("\nTesting BC3 sanitize_filename...")
    for input_name, expected in test_cases:
        actual = sanitize_bc3(input_name)
        print(f"  Input: '{input_name}' -> Actual: '{actual}' (Expected: '{expected}')")
        assert actual == expected

if __name__ == "__main__":
    test_sanitize()
    print("\nAll security tests passed!")
