import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP

MY_EMAIL = 'animashaunjamal700@gmail.com'
MY_PASSWORD = 'eompqxrifixxvwpr'

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = { 
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept-Language': 'en-US,en;q=0.5'
}


response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, 'lxml')
print(soup.prettify())

price = soup.find(class_='a-price-whole').getText()

print(price)

price_without_currency = price.split('$')[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < 100:
    with SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='devboybizarre@gmail.com', msg=f"Subject:Price Drop Alert!\n\nThe price of the product is now below $100")