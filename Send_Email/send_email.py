import smtplib
import ssl
from email.message import EmailMessage

subject = 'Email from Python'
body = 'This is a test email from Python!'
sender_email = 'python.505.test@gmail.com'
reciver_email = 'python.505.test@gmail.com'
password = input('Enter a password: ')

def send_email():
    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = reciver_email
    message['Subject'] = subject
    message.set_content(body)

    context = ssl.create_default_context()


    print('Sending Email')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciver_email, message.as_string())
    print('Success')

def send_html():
    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = reciver_email
    message['Subject'] = subject
    
    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """
    message.add_alternative(html, subtype='html')

    context = ssl.create_default_context()

    print('Sending Email')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciver_email, message.as_string())
    print('Success')

send_html()