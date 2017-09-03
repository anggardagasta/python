import smtplib
# ============ Simple sending email ================

# recipients = 'anggarda.gasta.p@mail.ugm.ac.id, anggarda.gasta.p@gmail.com'
# subject = 'TEST MAIL'
# text = 'Here is a message from python.'

# # Gmail Sign In
# sender = 'your_email@mail.com'
# password = 'your_email_password'

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()
# server.login(sender, password)

# body = '\r\n'.join(['To: %s' % recipients,
#                     'From: Anggarda Gasta <%s>' % sender,
#                     'Subject: %s' % subject,
#                     '', text])

# try:
#     server.sendmail(sender, recipients.split(','), body)
#     print ('email sent')
# except Exception as e:
#     print ('error sending mail', e)

# server.quit()

# ============ Email with attachment ================
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64
 
sender = "your_email@mail.com"
password = "your_email_password"

recipients = "anggarda.gasta.p@gmail.com, anggarda.gasta.p@mail.ugm.ac.id"
 
msg = MIMEMultipart()
 
msg['From'] = 'Anggarda Gasta <%s>' % sender
msg['To'] = recipients
msg['Subject'] = "SUBJECT OF THE EMAIL"
 
body = "TEXT YOU WANT TO SEND"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "test.csv"
attachment = open("files/data.csv", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

try:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	# login
	server.login(sender, password)
	text = msg.as_string()
	print ('Sending email...')
	server.sendmail(sender, recipients, text)
	server.quit()
except Exception as e:
	print ('error sending mail', e)

