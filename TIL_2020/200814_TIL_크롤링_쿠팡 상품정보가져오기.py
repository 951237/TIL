import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}


for i in range(1, 6):
    URL = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81" \
        f"&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter" \
        f"=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36" \
        f"&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=4&backgroundColor="


    res = requests.get(URL, headers=headers) # 쿠팡에서 크롤링 막음. 에이전트 삽입
    res.raise_for_status()  # 정보 가져오지 못하면 멈춤

    soup = BeautifulSoup(res.text, "lxml")  # 데이터 가져온것 lxml로 파싱하기

    items = soup.find_all("li", attrs={"class" : "search-product "})    # 노트북 큰
    # 덩어리 가져오기

    for item in items:
        ad = item.find("span", attrs={"class" : "ad-badge-text"})
        if ad:
            # print("         <광고 상품입니다.>")
            continue

        name = item.find("div", attrs={"class" : "name"}).get_text()    # 제목 가져오기
        if "Apple" in name:
            # print("         <애플 제품입니다.>")
            continue

        item_url = item.find("a", attrs={"class" : "search-product-link"})[
            "href"]  # a태그의 링크 가져오기
        link = "https://www.coupang.com" + item_url # 가져온 url에 쿠팡 주소붙여서 완성
        price = item.find("strong", attrs={"class" : "price-value"}).get_text() #가격태그의 텍스트 가져오기
        rate = item.find("em", attrs={"class" : "rating"}) # em태그 찾아서 rate에 저장
        if rate:    # rate가 있으면
            rate = rate.get_text()  # 평점 텍스트로 가져오기
        else:   # 없으면
            # print("평점이 없습니다.")
            continue

        rate_cnt = item.find("span", attrs={"class" : "rating-total-count"})
        #span태그에 평정수를 변수에 저장
        if rate_cnt: #평정수가 있으면
            rate_cnt = rate_cnt.get_text()[1:-1] #괄호 다음부터 괄호 마지막까지 텍스트 가져오기
        else:
            # print("평점수가 없습니다.")
            continue

        if float(rate) >= 4.5 and int(rate_cnt) > 80:
            print(f'제품명 : {name}')
            print(f'가격 : {price}')
            print(f'평점 : {rate}')
            print(f'평점수 : {rate_cnt}')
            print(f'제품링크 : {link}')
            print("-"*100)

    print("-" * 40, f"{i}페이지", "-"*40)
