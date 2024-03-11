import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# print(soup)

# article_tag = soup.find_all(name='span', class_='titleline')
# print(article_tag)

# for tag in article_tag:
#   print(tag.getText())
#   print(tag.get('href'))

a_tags = soup.select(selector='.titleline a')
# print(a_tags)

for tag in a_tags:
  
  print(tag)
  print(tag.string)
  print(tag.get('href'))
  # print(tag.get('href')[0])