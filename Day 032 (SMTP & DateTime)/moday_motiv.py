import smtplib
import datetime as dt
import random
from email_creds import my_email, password, rec_email

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user = my_email, password= password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=rec_email, 
                            msg = f"Subject:Here is your Monday Motivation!\n\n{quote}")