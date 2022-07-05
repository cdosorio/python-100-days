import lxml
import requests
from bs4 import BeautifulSoup

url = "https://typing-speed-test.aoeu.eu/"
response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, "lxml")

f = soup.find_all('span',attrs={'class':'nextword'})
for i in f:
    print(i.text)
