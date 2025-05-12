from bs4 import BeautifulSoup
import requests
import pandas as pd
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name='a')
#
# # for tag in all_anchor_tags:
# #     pass
# #     #print(tag.getText())
# #     #print(tag.get("href"))
# #
# # heading = soup.find(name="h1", id="name")
# # print(heading.getText())
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
#
# company_url = soup.select_one(selector="p a")
#
#
# name = soup.select_one(selector="#name")
#
#
# name = soup.select(selector=".heading")
# print(name.string)

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.find_all(name='a', class_='storylink')
article_text = [i.getText() for i in articles]
article_links = [i.get('href') for i in articles]
scores = soup.find_all(name='span', class_='score')
article_upvotes = [int(score.getText().split(' ')[0]) for score in scores]
data = pd.DataFrame({"article_text": article_text,
                     "article_links" : article_links,
                     "article_upvotes" : article_upvotes})
data.sort_values('article_upvotes',inplace=True,ascending=False)
print(data.iloc[0,:])
