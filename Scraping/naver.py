import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색을 원하는 키워드를 입력해주세요")

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap") # 결과물은 list 형태의 자료형으로 들어갑니다.

for i in results:
    title = i.select_one(".title_link").text  # i.select_one("실제 페이지의 class명")
    write = i.select_one(".name").text
    link = i.select_one(".title_link")["href"]
    dsc = i.select_one(".dsc_link").text
    print(f'제목 : {title}')
    print(f'작성자 : {write}')
    print(f'링크 : {link}')
    print(f'요약 : {dsc}')
    print("----------------------------------------")

# 광고글... 데이터 광고글 빼고 출력해!