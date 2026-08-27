'''                               PROJECT 6 - BULK EMAIL SENDER                                               '''

import smtplib # for sending emails
from email.message import EmailMessage # for creating email messages
import os # for file operations

# related to Object-Oriented Programming (OOP)
class EmailService:
    def __init__(self, sender_email, app_password):
        self.sender_email = sender_email
        self.app_password = app_password
        self.smtp_server = "smtp.gmail.com"
        self.port = 465 # SSL Port

    def send_email(self, recipient_email, subject, body):
        """Creates and sends an individual email."""
        msg = EmailMessage()
        msg["From"] = self.sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            # Connect to SMTP server over SSL
            with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:
                server.login(self.sender_email, self.app_password)
                server.send_message(msg)
                print(f"[DONE] Successfully sent email to {recipient_email}")
                
                # CH-8: Log the successful send to a file
                self.log_sent_email(recipient_email, subject)
                return True
        except Exception as e:
            print(f"[ERROR] Failed to send to {recipient_email}. Error: {e}")
            return False

    # related to File I/O
    def log_sent_email(self, recipient_email, subject):
        """Appends a record of the sent email to a log file."""
        with open("sent_emails_log.txt", "a") as file:
            file.write(f"Sent To: {recipient_email} | Subject: {subject}\n")


# Related Functions

#! NOTE - Replace with your actual app password then only run the script once to avoid exposing it in version control.
'''                  HOW TO GENERATE AN APP PASSWORD FOR GMAIL (IF 2-STEP VERIFICATION IS ENABLED)                      

1.) Enable 2-Step Verification: Go to your Google Account Security settings and ensure "2-Step Verification" is turned ON.

2.)Search for App Passwords: In the search bar at the top of the Google Account settings page, type "App passwords" and click on the result.

3.)Create the Password: It will ask you to provide a name for the app. Type something like "Python Script" and click Create.
Google will generate a 16-character password in a yellow box (e.g., abcd efgh ijkl mnop).

4.) Update Your Code:

4.1) Copy that 16-character password (you can remove the spaces).
4.2)Go back to your E-mail.py file in VS Code.
4.3)Replace "your_16_char_app_password" with this new code. Make sure your actual Gmail address is also updated in the SENDER variable.

Once you paste the App Password into your code and save the file, run it again. The terminal should print done Successfully sent email!'''

def run_bulk_emailer():
    # --- Authentication Details ---
    # NOTE: Use an App Password if using Gmail, not your normal password!
    SENDER = "tanmay.w119@gmail.com"
    APP_PASSWORD = "xyz1 23ab c456"  # Replace with your actual app password


# Instantiate the EmailService object (CH-9)
    service = EmailService(sender_email=SENDER, app_password=APP_PASSWORD)

    # related to Lists of Dictionaries
    recipients = [
        {"name": "Alice", "email": "alice@example.com", "project": "QR Generator"},
        {"name": "Bob", "email": "bob@example.com", "project": "Weather Checker"},
        {"name": "Charlie", "email": "charlie@example.com", "project": "Portfolio Website"},
    ]

    # related to Loops & CH-2: Strings Formatting
    for person in recipients:
        # Dynamic f-string customization (CH-2)
        subject_line = f"Update on your project: {person['project']}"
        
        email_body = f"""Hello {person['name']},

Thank you for your hard work on {person['project']}.
Your submission has been reviewed successfully!

Best regards,
Python Team
"""
        # Call the class method to send the email
        service.send_email(person["email"], subject_line, email_body)


if __name__ == "__main__":
    run_bulk_emailer()