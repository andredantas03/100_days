import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
names = soup.find_all(name='h3', class_='title')
names_list = [i.getText() for i in names]
names_list = names_list[::-1]

with open("movies.txt","a+",encoding="utf-8") as file:
    for i in range(len(names_list)):
        print(i)
        file.write(f'{names_list[i]}\n')


