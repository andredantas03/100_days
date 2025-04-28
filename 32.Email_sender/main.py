##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import random as rd
import smtplib
import os

today = str(dt.datetime.now().month)+"-"+str(dt.datetime.now().day)

birthdays = pd.read_csv("birthdays.csv")

birthdays["birthday"] = (birthdays["month"].astype(str) +"-"+ birthdays["day"].astype(str))

for index,item in birthdays[birthdays["birthday"].isin([today])].iterrows():
    template = rd.choice(os.listdir("letter_templates/"))
    with open(f"letter_templates/{template}","r") as file:
        msg = file.read().replace("[NAME]",item['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="appbirthday9@gmail.com",password="jrwpkvgsduuhvjrw")
        connection.sendmail(from_addr="appbirthday9@gmail.com",
                            to_addrs=item.email,
                            msg=f"Subject:Hello!\n\n{msg}"
                            )



