import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50") # 리스트와 동일한 형태라 인덱스를 가지고 있다.
lst100 = soup.select(".lst100") # 리스트와 리스트를 합치는 방법에 대해서 배웠다 ~> "+"
lst_all = lst50 + lst100

# 순위
# 제목(text) ellipsis rank01
# 가수(text) ellipsis rank02
# 앨범(text) ellipsis rank03
for rank, i in enumerate(lst_all, 1): 
    title = i.select_one(".ellipsis.rank01 a").text  
    singer = i.select_one(".ellipsis.rank02 a").text
    album = i.select_one(".ellipsis.rank03 a").text
    ## python으로 해결 -> strip() : 불필요한 공백이나 줄 바꿈 문자 등을 제거해 깔끔한 텍스트만 출력해주는 것 

    print(f"[순위]: {rank}")
    print(f"[제목] : {title}")
    print(f"[가수] :{singer}")
    print(f"[앨범] : {album}")
    print()
