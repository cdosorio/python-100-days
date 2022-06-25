from bs4 import BeautifulSoup

import requests
# -------------------------- DIRECT WEBSITE SCRAPING -------------------------------- #
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

# First article
# article_tag = soup.find(name="a", class_="titlelink")
# article_text = article_tag.getText()
# print(article_text)

# article_link = article_tag.get('href')
# print(article_link)
# article_id = soup.find(name='tr', class_='athing').get('id')
# article_score = soup.find(name='span', id=f'score_{article_id}').getText()
# print(article_score)


# highest scoring article
article_tags = soup.find_all(name="a", class_="titlelink")
article_text_list = []
article_url_list = []

for tag in article_tags:
    article_text_list.append(tag.getText())
    article_url_list.append(tag.get('href'))

article_ids = [each_id.get('id') for each_id in soup.find_all(name='tr', class_='athing')]
article_score_list = []

for each_id in article_ids:
    try:
        article_score_list.append(int(soup.find(name='span', id=f'score_{each_id}').getText().split()[0]))
    except AttributeError:
        article_score_list.append(0)

highest_score_index = article_score_list.index(max(article_score_list))
print(f"{article_text_list[highest_score_index]}\nURL: {article_url_list[highest_score_index]} Score: {article_score_list[highest_score_index]}")