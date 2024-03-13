# import smtplib
import datetime as dt

# smtp.mail.yahoo.com
# smtp.gmail.com

# MY_EMAIL = 'animashaunjamal700@gmail.com'
# MY_PASSWORD = 'eompqxrifixxvwpr'
# MSG = 'Subject:Hello there\n\nHow are you doing? \nNice to meet you'


# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls() # securing and encrypting the connection
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL, to_addrs='devboybizarre@gmail.com', msg=MSG)

# print('This email has been sent!')

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()


date_of_birth = dt.datetime(year=1988, month=12, day=6, hour=4, minute=45, second=12)
# print(type (now_time.year))
print(day_of_week)
print(date_of_birth)