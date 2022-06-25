from bs4 import BeautifulSoup

import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

all_titles = soup.find_all(name="h3", class_="title")

titles_list = [title.getText() for title in all_titles]
titles_list = titles_list[::-1] #splice to reverse list
print(titles_list)


# with open("top100.txt", mode="w") as file:
#     for title in reversed(all_titles):
#         #print(title.getText())
#         file.write(f"\n{title.getText()}")

        
