import sys
import os

# Add the current directory to sys.path to import extractor
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from extractor import sanitize_filename
except ImportError:
    # Fallback if import fails during initial setup
    import re
    def sanitize_filename(name):
        return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def test_security():
    print("Running security tests for sanitize_filename...")

    # We want to ensure that sanitize_filename:
    # 1. Removes path traversal characters (.., /)
    # 2. Removes invalid characters
    # 3. Does not return an empty string (DoS or unexpected behavior)
    # 4. Does not return only dots

    test_cases = [
        ("Normal Title", "Normal Title"),
        ("Title/With/Slashes", "TitleWithSlashes"),
        ("Title\\With\\Backslashes", "TitleWithBackslashes"),
        ("..", "unnamed"),
        ("../../etc/passwd", "etcpasswd"),
        ("..\\..\\etc\\passwd", "etcpasswd"),
        (".", "unnamed"),
        ("./hidden", "hidden"),
        ("   ", "unnamed"),
        ("", "unnamed"),
        ("file.ext", "fileext"), # We might want to keep the dot for extensions, but Basecamp titles don't usually have them as part of path
    ]

    # Note: Current implementation will FAIL many of these.
    # That's expected as we are writing the test BEFORE the fix.

    success = True
    for input_val, expected in test_cases:
        try:
            actual = sanitize_filename(input_val)
            if actual == expected:
                print(f"  [PASS] '{input_val}' -> '{actual}'")
            else:
                print(f"  [FAIL] '{input_val}' -> '{actual}' (Expected: '{expected}')")
                success = False
        except Exception as e:
            print(f"  [ERROR] '{input_val}' raised exception: {e}")
            success = False

    if not success:
        print("\nSecurity tests failed! (Expected before the fix)")
        # We don't exit 1 here yet because we want to see the failures first
    else:
        print("\nSecurity tests passed!")

if __name__ == "__main__":
    test_security()
