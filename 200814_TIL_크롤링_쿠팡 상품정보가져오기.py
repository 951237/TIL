import requests
from bs4 import BeautifulSoup

URL = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
res = requests.get(URL, headers=headers) 
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class" : "search-product "})

for item in items:
    name = item.find("div", attrs={"class" : "name"}).get_text()
    item_url = item.find("a", attrs={"class" : "search-product-link"})["href"]
    link = "https://www.coupang.com" + item_url
    price = item.find("strong", attrs={"class" : "price-value"}).get_text()
    rate = item.find("em", attrs={"class" : "rating"})
    if rate:
        rate = rate.get_text()
    else:
        print("평점이 없습니다.")
    rate_cnt = item.find("span", attrs={"class" : "rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()[1:-1]
    else:
        "평점수가 없습니다."

    print(name, price, rate, rate_cnt, link)