from bs4 import BeautifulSoup


with open('website.html') as file:
  contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

for tag in all_anchor_tags:
  # print(tag.getText())
  print(tag.get('href'))

h1_heading = soup.find(name='h1', id='name')
print(h1_heading)


h3_heading = soup.find(name='h3', class_='heading')
print(h3_heading)

# select nested html elements
company_url = soup.select_one(selector='p a')
print(company_url)

# select by id
name = soup.select_one(selector='#name')
print(name)

# select by class
headings = soup.select(selector='.heading')
print(headings)