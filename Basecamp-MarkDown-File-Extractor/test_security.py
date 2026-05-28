import os
import sys
from pathlib import Path

# Add the directory containing extractor.py to the search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from extractor import sanitize_filename
except ImportError:
    print("Error: Could not import sanitize_filename from extractor.py")
    sys.exit(1)

def test_path_traversal():
    EXPORTS_DIR = Path("/tmp/Basecamp-Exports")

    # Test cases: (input, expected_sanitized)
    test_cases = [
        ("../../../etc/passwd", "etcpasswd"),
        ("..", "unnamed"),
        (".ssh/authorized_keys", "sshauthorized_keys"),
        ("normal project title", "normal project title"),
        ("project...title", "project.title"),
        ("   ", "unnamed"),
        ("...leading dots", "leading dots"),
    ]

    print("Running Security Tests for filename sanitization...")
    for malicious_title, expected in test_cases:
        sanitized = sanitize_filename(malicious_title)
        print(f"Input: {malicious_title!r} -> Sanitized: {sanitized!r}")

        # Check if it stays within EXPORTS_DIR
        full_path = os.path.join(str(EXPORTS_DIR), sanitized)
        normalized = os.path.normpath(full_path)
        if not normalized.startswith(str(EXPORTS_DIR)):
            print(f"  FAILED: PATH TRAVERSAL DETECTED for {malicious_title!r} -> {normalized}")
            sys.exit(1)
        elif ".." in sanitized or sanitized.startswith("/"):
            print(f"  FAILED: Sanitized name {sanitized!r} still contains traversal characters")
            sys.exit(1)
        else:
            print(f"  PASSED")

    print("\nAll security tests passed!")

if __name__ == "__main__":
    test_path_traversal()
