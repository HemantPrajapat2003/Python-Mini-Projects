import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# =========================================
# SENDER EMAIL DETAILS
# =========================================

from_addr = "yourgmail@gmail.com"
password = "your_app_password"

# =========================================
# READ CSV FILE
# =========================================

# CSV file format:
# name,email
# Hemant,hemant@gmail.com
# Rahul,rahul@yahoo.com

data = pd.read_csv("abc.csv")

# Get columns from CSV
names = data['name'].tolist()
emails = data['email'].tolist()

# =========================================
# CONNECT TO GMAIL SMTP SERVER
# =========================================

try:
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()

    # Login to Gmail
    mail.login(from_addr, password)

    print("Login Successful\n")

    # =========================================
    # SEND EMAILS
    # =========================================

    for i in range(len(emails)):

        # Create Message Object
        msg = MIMEMultipart()

        # Email Details
        msg['From'] = from_addr
        msg['To'] = emails[i]
        msg['Subject'] = "Welcome Email"

        # Email Body
        body = f"""
Hello {names[i]},

This is a test email sent using Python.

Thank You
Hemant
"""

        # Attach Body
        msg.attach(MIMEText(body, 'plain'))

        # Convert message to string
        text = msg.as_string()

        # Send Email
        mail.sendmail(from_addr, emails[i], text)

        print(f"Email sent to: {emails[i]}")

    # =========================================
    # CLOSE SMTP CONNECTION
    # =========================================

    mail.quit()

    print("\nAll Emails Sent Successfully")

except Exception as e:
    print("Error:", e)