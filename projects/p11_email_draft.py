from pathlib import Path
from email.message import EmailMessage
import argparse
import os
import smtplib
import ssl

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "output" / "project_11" / "status_email.eml"

def compose():
    message = EmailMessage()
    message["From"] = os.getenv("SENDER_EMAIL", "sender@example.com")
    message["To"] = os.getenv("TEST_TO_EMAIL", "recipient@example.com")
    message["Subject"] = "Weekly report is ready"
    message.set_content("Hello,\n\nThe weekly report is ready for review.\n\nRegards")
    return message

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--send", action="store_true", help="Actually send mail")
    args = parser.parse_args()
    msg = compose()
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(msg.as_bytes())
    if not args.send:
        print(f"Saved draft to {DEST}; no email was sent.")
        return
    host = os.environ["SMTP_HOST"]
    port = int(os.environ.get("SMTP_PORT", "465"))
    user = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASSWORD"]
    if "example.com" in str(msg["To"]) or "example.com" in str(msg["From"]):
        raise ValueError("Set real test sender and recipient addresses")
    with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context()) as server:
        server.login(user, password)
        server.send_message(msg)
    print("Sent test email to the configured recipient.")

if __name__ == "__main__":
    main()
