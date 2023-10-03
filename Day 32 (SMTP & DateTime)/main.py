# import smtplib

# from email import password, my_email, rec_email

# with smtplib.SMTP('smtp.gmail.com',587) as connection:

#     #This encrypts our email
#     connection.starttls()
#     connection.login(user = my_email, password= password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=rec_email, 
#                         msg = "Subject:Hello!\n\nHello World")




############################ Date Time ################################
import datetime as dt

now = dt.datetime.now()
year = now.year
print(year) #datatype is an int
print(now)  #datatype is a str

date_of_birth = dt.datetime(year = 1995, month = 12, day =15, hour= 4)

print(date_of_birth)