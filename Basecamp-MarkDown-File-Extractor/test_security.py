import sys
import os

# Add the script directory to sys.path to import extractor
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extractor import sanitize_filename

def test_sanitize_filename():
    print("Running security tests for sanitize_filename...")
    test_cases = [
        ("Normal Title", "Normal Title"),
        ("Title/With/Slashes", "TitleWithSlashes"),
        ("../../etc/passwd", "etcpasswd"),
        ("...", "unnamed"),
        (".", "unnamed"),
        ("", "unnamed"),
        ("   ", "unnamed"),
        ("Con: In/Out?", "Con InOut"),
        ("Hidden.file", "Hiddenfile"),
    ]

    for input_name, expected in test_cases:
        result = sanitize_filename(input_name)
        assert result == expected, f"Failed for '{input_name}': expected '{expected}', got '{result}'"
        print(f"  [PASS] '{input_name}' -> '{result}'")

    print("\nAll security tests passed!")

if __name__ == "__main__":
    try:
        test_sanitize_filename()
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")
        sys.exit(1)
