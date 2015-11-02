import smtplib


# Create stmp connection obj
# SMTP Servers: Gmail smtp.gmail.com; outlook/hotmail: smtp-mail.outlook.com; 
# Yahoo: smtp.mail.yahoo.com; port is usually 587
conn = smtplib.SMTP('smtp.gmail.com', 587)
# Connect to the email server
conn.ehlo()
# Start encrytion in order to login
conn.starttls()
# Login, gmail use application specific password
conn.login('username@gmail.com', 'password')

# Send email, return value of sendmail is dict with all failed emails
conn.sendmail('fromaddress', 'toaddress', 'Subject: subject \n\nMain body for the email\n\n')
# Disconnect the connection
conn.quit()
