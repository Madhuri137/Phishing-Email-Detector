# 📧 Phishing Email Detector

A Python-based tool to detect phishing emails using **regex, keyword analysis, link validation, and attachment scanning**.  
It helps identify suspicious sender addresses, urgency keywords, mismatched links, and risky attachments.  
This project demonstrates cybersecurity fundamentals and is ideal for practical learning and showcasing in resumes/LinkedIn.

---

## 🚀 Features
- Detects suspicious sender domains (e.g., `paypa1.com` instead of `paypal.com`)
- Flags urgency keywords: *urgent*, *verify*, *immediately*, *account suspended*
- Analyzes links for mismatches between visible text and actual URL
- Identifies risky attachments (e.g., `.zip` files)
- Generates a clear report with detected phishing indicators

---

## 🛠️ Technologies Used
- **Python 3**
- **Regex (Regular Expressions)**
- **Email parsing**
- **File handling**

---

## 📂 Project Structure
Phishing-Email-Detector/
├── README.md                # Documentation
├── src/                     # Source code
│   ├── run_detector.py       # Main entry point
│   ├── detection.py          # Phishing checks (sender, links, urgency, etc.)
│   ├── email_parser.py       # Email parsing logic
│   └── report.py             # Report generation
└── samples/                 # Example email files
    ├── sample_email.eml
    ├── email_3.eml
    └── email_4.eml


---

## 🖥️ Usage

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Madhuri137/Phishing-Email-Detector.git
   cd Phishing-Email-Detector

