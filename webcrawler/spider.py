import requests
from bs4 import BeautifulSoup

def trade_spider (max_pages):
    page=2
    while page <= max_pages:
        url= "http://www.patogupirkti.lt/Leidyklos-VAGA-knygu-ispardavimas/"+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all("div", {"class":"item list free-delivery-container"}):
            title = link.get("data-title")
            price = link.get("data-price")
            print(title+price)
        page +=1



trade_spider(6)
