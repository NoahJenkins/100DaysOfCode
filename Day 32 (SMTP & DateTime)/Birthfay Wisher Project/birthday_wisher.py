import smtplib
import random
import random
import datetime as dt
import pandas
from email_creds import password, my_email
now = dt.datetime.now()
today = (now.month, now.day)
print(today)

data = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1-3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user = my_email, password= password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'] 
                            msg = f"Subject:Happy Birthday!\n\n{contents}")


