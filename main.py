from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")

all_title = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article_tag in all_title:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    link = article_tag.find('a').get("href")
    article_links.append(link)

points = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

most_points = max(points)
largest_index = points.index(most_points)

print(article_texts[largest_index])
print(article_links[largest_index])
print(most_points)


