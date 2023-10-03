import smtplib

my_email = "dev892259@gmail.com"
from password import password

connection = smtplib.SMTP('smtp.gmail.com')

#This encrypts our email
connection.starttls()
connection.login(user = my_email, password= password)
connection.sendmail(from_addr=my_email, to_addrs="dev.two@yahoo.com", mesg = "Hello World")
connection.close()