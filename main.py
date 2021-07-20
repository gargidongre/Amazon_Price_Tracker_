import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.in/ADISA-SL5008-black-women-quilted/dp/B078JNB821/ref=sr_1_6?dchild=1&keywords=sling+bags&qid=1615954123&sr=8-6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language" :"en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
webpage_html = response.content


soup = BeautifulSoup(webpage_html, "lxml")
price = soup.find(id="priceblock_dealprice").get_text()
price_without_currency = price.split("₹")[1]
float_price = float(price_without_currency)
print(float_price)
