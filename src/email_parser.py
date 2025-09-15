# email_parser.py
from email import message_from_file

def read_email(file_path):
    """Return a dict with keys: 'from', 'subject', 'body' (simple)."""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        msg = message_from_file(f)
    sender = msg.get("From", "")
    subject = msg.get("Subject", "")
    # get_payload may return list for multipart; handle simply:
    body = ""
    if msg.is_multipart():
        parts = []
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    parts.append(part.get_payload(decode=True).decode(errors="ignore"))
                except:
                    parts.append(str(part.get_payload()))
        body = "\n".join(parts)
    else:
        try:
            body = msg.get_payload(decode=True).decode(errors="ignore")
        except:
            body = str(msg.get_payload())
    return {"from": sender, "subject": subject, "body": body}

