import lxml
import requests
from bs4 import BeautifulSoup

_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "Accept-Language":"es-US,es;q=0.9,en-US;q=0.8,en;q=0.7"
    }
url = "https://www.amazon.com/dp/B08WZXP336/ref=cm_sw_em_r_mt_dp_K8TH64VTGTF9PD40F7ZA?_encoding=UTF8&psc=1"

response = requests.get(url, headers=_headers)
amazon_product = response.text
#print(amazon_product)
soup = BeautifulSoup(amazon_product, "lxml")
tag_price = soup.find(name='span', class_='a-offscreen')
text_price = tag_price.getText()
price = float(text_price.replace("$", ""))
print(price)