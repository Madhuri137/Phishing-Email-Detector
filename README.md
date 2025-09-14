# Phishing Email Detector

A Python-based tool that detects phishing emails using **regex, keyword analysis, link validation, and attachment scanning**.

## Features
- Detects suspicious sender domains (e.g., `paypa1.com`)
- Flags urgency keywords: "urgent", "verify", "immediately"
- Analyzes links for mismatches between visible text and actual URL
- Identifies risky attachments like `.zip` files
- Generates a report with detected phishing indicators

## Technologies Used
- Python 3
- Regex (Regular Expressions)
- Email parsing
- File handling

## Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Phishing-Email-Detector.git
   cd Phishing-Email-Detector
