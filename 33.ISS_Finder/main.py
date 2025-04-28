import smtplib
import requests
from datetime import datetime
import time

MY_LAT = -3.718460 # Your latitude
MY_LONG = -38.541672 # Your longitude

def isissnear():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_distance = abs(iss_latitude - MY_LAT)
    lng_distance = abs(iss_longitude - MY_LONG)
    if lat_distance <= 5 and lng_distance <= 5:
        return True
    else:
        return False

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour<=sunrise:
        return True
    else: return False


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



while True:
    print("ahoy!")
    if is_night() and isissnear():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="appbirthday9@gmail.com", password="jrwpkvgsduuhvjrw")
            connection.sendmail(from_addr="appbirthday9@gmail.com",
                                to_addrs="andredantas003@gmail.com",
                                msg=f"Subject:Look Up!\n\n The ISS is above you in the sky!"
                                )
    time.sleep(60)



