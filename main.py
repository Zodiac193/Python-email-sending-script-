from email.message import EmailMessage
import smtplib
import ssl

# Email Sender Specs
email_sender = 'medom193@gmail.com'
email_password = 'ptzeqcasjzoifaht'

# Email Specs
email_subject = 'Coding Skills'
email_body = '''
improving Python Coding Skills By Building Projects
'''

# Email Receiver Specs
email_receiver = 'wijaj61134@chotunai.com'

# setting Up the email
em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = email_subject
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


