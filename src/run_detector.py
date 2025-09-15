from email_parser import read_email
from detection import run_all_checks
from report import generate_report
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_detector.py <email_file>")
        return

    file_path = sys.argv[1]
    email = read_email(file_path)
    results = run_all_checks(email)

    # 🔹 Debug print to see what body looks like
    print("=== DEBUG BODY ===")
    print(email["body"])
    print("=== END BODY ===")

    generate_report(email, results)

if __name__ == "__main__":
    main()
