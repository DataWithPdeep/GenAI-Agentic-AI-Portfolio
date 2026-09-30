import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from langchain_core import tool

smtp_server = "smtp.gmail.com"
smtp_port = 587

sender_email = "psrana344@gmail.com"
password = "hlib gygs wclv szhx"


def send_email_by_gmail(to: str, subject: str, body_text: str):

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = to
    message["Subject"] = subject

    message.attach(MIMEText(body_text, "plain"))

    server = None

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)

        server.starttls()

        server.login(sender_email, password)

        print("Login successful. Sending email....")

        server.sendmail(
            sender_email,
            to,
            message.as_string()
        )

        print("Email sent successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if server:
            server.quit()


@tool
def send_email(to: str, subject: str, body: str)-> str:
    """
        Send an email to any email address.

    Args:
        to: The recipient's email address.
        subject: The email subject.
        body: The email body in plain text.
    """
    send_email_by_gmail(to=to,
        subject=subject,
        body_text=body)
    return "Email Send Successfully..."


ALL_TOOLS = [send_email]


