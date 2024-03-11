import requests
import time
from smtplib import SMTP
from datetime import datetime

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)

# print(iss_position)
# print(data)
# print(response.status_code)



MY_EMAIL = 'animashaunjamal700@gmail.com'
MY_PASSWORD = 'eompqxrifixxvwpr'
MY_LAT = 6.524379
MY_LONG = 3.379206


def is_iss_overhead():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_longitude = float(iss_data['iss_position']['longitude'])
    iss_latitude = float(iss_data['iss_position']['latitude'])

    # your position is within +5 or -5 degrees of the iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
      "lat": 6.524379,
      "lng": 3.379206,
      "formatted": 0,
    }

    sun_response = requests.get(url=f'https://api.sunrise-sunset.org/json', params=parameters)
    sun_response.raise_for_status()

    sun_data = sun_response.json()

    sunrise = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs='devboybizarre@gmail.com', msg="Subject:Look Up 👆🏽\n\nThe Iss is above you in the sky")
