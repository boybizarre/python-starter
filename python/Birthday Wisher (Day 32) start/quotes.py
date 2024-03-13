import smtplib
import datetime as dt
import random

MY_EMAIL = 'animashaunjamal700@gmail.com'
MY_PASSWORD = 'eompqxrifixxvwpr'

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 3:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='devboybizarre@gmail.com', msg=f'Subject:Monday Motivation\n\n{quote}')
    