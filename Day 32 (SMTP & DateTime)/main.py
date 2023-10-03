import smtplib

my_email = "dev892259@gmail.com"
password = "abc123"

connection = smtplib.SMTP('smtp.gmail.com')

#This encrypts our email
connection.starttls()
connection.login(user = my_email, password= password)
con