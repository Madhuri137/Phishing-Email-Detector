# Phishing Email Detector

A Python-based tool to detect phishing emails using **regex, keyword analysis, link validation, and attachment scanning**.  
It helps identify suspicious sender addresses, urgency keywords, mismatched links, and risky attachments.  
This project demonstrates cybersecurity fundamentals and is ideal for practical learning and showcasing in resumes/LinkedIn.

---

##  Features
- Detects suspicious sender domains (e.g., `paypa1.com` instead of `paypal.com`)
- Flags urgency keywords: *urgent*, *verify*, *immediately*, *account suspended*
- Analyzes links for mismatches between visible text and actual URL
- Identifies risky attachments (e.g., `.zip` files)
- Generates a clear report with detected phishing indicators

---

##  Technologies Used
- **Python 3**
- **Regex (Regular Expressions)**
- **Email parsing**
- **File handling**

---

##  Project Structure
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

##  Usage

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Madhuri137/Phishing-Email-Detector.git
   cd Phishing-Email-Detector

Example:

C:\Users\molis\Desktop\Phising-email-detector>python run_detector.py samples\sample_email.eml
=== DEBUG BODY ===
Dear user,

Please verify your account immediately by clicking the link below:
http://fake-paypa1.com/login

Thanks,
Support Team

=== END BODY ===

=== Email Summary ===
From: fake@paypa1.com
Subject: Verify your account now

⚠️ Suspicious Indicators Found:
1. Suspicious sender: possible spoofing of PayPal domain
2. Suspicious link detected: http://fake-paypa1.com/login
3. Urgency tactic detected in body: 'immediately'
4. Urgency tactic detected in subject: 'verify'
5. Urgency tactic detected in body: 'verify'
