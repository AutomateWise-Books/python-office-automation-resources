from pathlib import Path
from email.message import EmailMessage
import argparse
import mimetypes
import os
import smtplib
import ssl

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "samples" / "project_12" / "attachment.pdf"
DEST = ROOT / "output" / "project_12" / "email_with_attachment.eml"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--send", action="store_true")
    args = parser.parse_args()
    message = EmailMessage()
    message["From"] = os.getenv("SENDER_EMAIL", "sender@example.com")
    message["To"] = os.getenv("TEST_TO_EMAIL", "recipient@example.com")
    message["Subject"] = "Document for review"
    message.set_content("Please find the sample document attached.")
    main_type, sub_type = (mimetypes.guess_type(FILE.name)[0] or
                           "application/octet-stream").split("/", 1)
    message.add_attachment(FILE.read_bytes(), maintype=main_type,
                           subtype=sub_type, filename=FILE.name)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(message.as_bytes())
    if not args.send:
        print(f"Saved an email draft with attachment to {DEST}; not sent.")
        return
    if "example.com" in str(message["To"]) or "example.com" in str(message["From"]):
        raise ValueError("Use a real test sender and recipient")
    with smtplib.SMTP_SSL(os.environ["SMTP_HOST"],
                          int(os.environ.get("SMTP_PORT", "465")),
                          context=ssl.create_default_context()) as server:
        server.login(os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"])
        server.send_message(message)
    print("Sent the test email with attachment.")

if __name__ == "__main__":
    main()
