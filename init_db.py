import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbOlympic


# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

driver = webdriver.Chrome('D:\Project\chromedriver_win32\chromedriver', options=options)
driver.implicitly_wait(3)

list_OlympicItem = ["KTE", "GLF", "MPN", "BSK", "RUG", "WRE", "VOL", "BDM", "BOX", "SHO", "CYC", "SRF", "AQU", "SKB", "CLB", "EQU",
 "BSB", "ARC", "WLF", "SAL", "JUD", "ATH", "ROW", "GYM", "FBL", "CAS", "TTE", "TKW", "TEN", "TRI", "FEN", "HOC", "HBL"]

list_OlympicItemKor = ["가라테", "골프", "근대5종", "농구", "럭비", "레슬링", "배구", "배드민턴", "복싱", "사격", "사이클", "서핑", "수영", "스케이딩 보딩", "스포츠 클라이밍", "승마",
 "야구 / 소프트볼", "양궁", "역도", "요트", "유도", "육상", "조정", "체조", "축구", "카누", "탁구", "태권도", "테니스", "트라이애슬론", "펜싱", "하키", "핸드볼"]




# DB에 저장할 경기 일정의 출처 url을 가져옵니다.
def init_items():

    # for i in range(len(list_OlympicItem)):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        
        driver.get('https://m.sports.naver.com/tokyo2020/schedule/index?type=discipline&date=&disciplineId=' + list_OlympicItem[0] + '&isKorean=Y')
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # divs = soup.select('#content > div > div > div.Schedule_game_schedule__1k6hJ > ul > li:nth-child(1) > ul > li > a')
        
        print(soup)

        # print(divs)
        # html = driver.page_source
        # soup = BeautifulSoup(html, 'html.parser')
        # divs = soup.select('#content')
        # data = requests.get('https://m.sports.naver.com/tokyo2020/schedule/index?type=discipline&date=&disciplineId=' + list_OlympicItem[i] + '&isKorean=Y', headers=headers)

        # data.encoding = 'utf-8'
        # soup = BeautifulSoup(data.text, 'html.parser')

        # divs = soup.select('#root')
        # divs = soup.select('.Schedule_game_schedule__1k6hJ')

        # for div in divs:
        #     print(div)

        # name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
        # img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
        # recent_work = soup.select_one(
        # '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

        doc = {
        'name': 0,
        'id': 0,
        'date': 0,
        'day': 0,
        'time': 0,
        'title': 0,
        'matchState': 0,
        'entry': 0,
        'matchResult': 0,
    }

        db.dbPlan.insert_one(doc) 
        # print('완료!')


# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
    db.dbPlan.drop()  # mystar 콜렉션을 모두 지워줍니다.

### 실행하기
insert_all()
init_items()
