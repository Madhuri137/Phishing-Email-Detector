import re

def check_sender(sender):
    issues = []
    if sender and "paypa1" in sender.lower():
        issues.append("Suspicious sender: possible spoofing of PayPal domain")
    return [(True, issue) for issue in issues]


def check_links(body):
    issues = []
    urls = re.findall(r'http[s]?://\S+', body)
    for url in urls:
        if "paypal.com" not in url and "paypa1.com" in url:
            issues.append(f"Suspicious link detected: {url}")
    return [(True, issue) for issue in issues]


def check_urgency(email_dict):
    issues = []
    urgent_words = ["urgent", "immediately", "verify", "act now", "account suspended"]

    subject = email_dict.get("subject", "").lower()
    body = email_dict.get("body", "").lower()

    for word in urgent_words:
        if word in subject:
            issues.append(f"Urgency tactic detected in subject: '{word}'")
        if word in body:
            issues.append(f"Urgency tactic detected in body: '{word}'")
    return [(True, issue) for issue in issues]


def check_attachments(body):
    issues = []
    dangerous_ext = [".exe", ".scr", ".js", ".vbs", ".zip", ".rar"]
    for ext in dangerous_ext:
        if ext in body.lower():
            issues.append(f"Suspicious attachment detected: *{ext}* file")
    return [(True, issue) for issue in issues]


def check_link_mismatch(body):
    issues = []

    # Markdown-style [text](url)
    pattern_md = re.findall(r'\[([^\]]+)\]\((http[s]?://[^\)]+)\)', body)
    for text, url in pattern_md:
        if text.strip().lower() not in url.strip().lower():
            issues.append(f"Link mismatch: text '{text}' points to '{url}'")

    # HTML-style <a href="url">text</a>
    pattern_html = re.findall(r'<a[^>]+href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>', body, re.IGNORECASE)
    for url, text in pattern_html:
        if text.strip().lower() not in url.strip().lower():
            issues.append(f"HTML Link mismatch: visible text '{text}' vs actual '{url}'")

    return [(True, issue) for issue in issues]


def run_all_checks(email_dict):
    checks = []
    checks.extend(check_sender(email_dict.get("from", "")))
    checks.extend(check_links(email_dict.get("body", "")))
    checks.extend(check_urgency(email_dict))
    checks.extend(check_attachments(email_dict.get("body", "")))
    checks.extend(check_link_mismatch(email_dict.get("body", "")))
    return checks
