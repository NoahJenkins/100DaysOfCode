import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from email import password, my_email, rec_email
import time
from datetime import datetime, timedelta



url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


from email_creds import password, my_email, rec_email

while True:
    now = datetime.now()
    target_time = datetime(now.year, now.month, now.day, 0, 0, 0)  # Set the target time to 12:00 AM

    if now >= target_time:
        if price_as_float <= 100:
            with smtplib.SMTP('smtp.gmail.com',587) as connection:
                #This encrypts our email
                connection.starttls()
                connection.login(user = my_email, password= password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=rec_email, 
                                    msg = f"Subject:Amazon Price Alert!!\n\nThe price of the item you have been watching is down to ${price_as_float})!")