import requests

URL = "https://www.naver.com"

res = requests.get(URL)

res.raise_for_status()

with open('naver.html', 'w', encoding='utf8') as f:
    f.write(res.text)
