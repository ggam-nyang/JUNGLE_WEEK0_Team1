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
driver.implicitly_wait(5)

list_OlympicItem = ["KTE", "GLF", "MPN", "BSK", "RUG", "WRE", "VOL", "BDM", "BOX", "SHO", "CYC", "SRF", "AQU", "SKB", "CLB", "EQU",
 "BSB", "ARC", "WLF", "SAL", "JUD", "ATH", "ROW", "GYM", "FBL", "CAS", "TTE", "TKW", "TEN", "TRI", "FEN", "HOC", "HBL"]

list_OlympicItemKor = ["가라테", "골프", "근대5종", "농구", "럭비", "레슬링", "배구", "배드민턴", "복싱", "사격", "사이클", "서핑", "수영", "스케이딩 보딩", "스포츠 클라이밍", "승마",
 "야구 / 소프트볼", "양궁", "역도", "요트", "유도", "육상", "조정", "체조", "축구", "카누", "탁구", "태권도", "테니스", "트라이애슬론", "펜싱", "하키", "핸드볼"]




# DB에 저장할 경기 일정의 출처 url을 가져옵니다.
def init_items():

    # for i in range(len(list_OlympicItem)):
        
        driver.get('https://m.sports.naver.com/tokyo2020/schedule/index?type=discipline&date=&disciplineId=' + list_OlympicItem[32] + '&isKorean=Y')
        soup = BeautifulSoup(driver.page_source, 'html.parser')


        # matchResult Data 가져오기
        test = driver.find_elements_by_class_name("GameScheduleList_status__3zxOL")
        # test2 = driver.find_elements_by_xpath('//*[@id="content"]/div/div[2]/div[3]/ul/li[1]/div/span')
        # test2 = driver.find_elements_by_css_selector('#content > div > div.Schedule_main_section__1SpMt > div:nth-child(3) > ul > li.GameScheduleList_game_item__2ricE > div > span')
        for i in test:
            print(i.text)
        


        # Time Data 가져오기
        # test = driver.find_elements_by_class_name("GameScheduleList_game_time__10dNy")

        # for i in test:
        #     print(i.text)


        # entry Data 가져오기
        # test = driver.find_elements_by_class_name("GameScheduleList_link_name__xBm7W")

        # for i in test:
        #     print(i.text)

        # date Data 가져오기
        # test = driver.find_elements_by_class_name("Schedule_date__iFiUq")

        # for i in test:
        #     print(i.text)


        # Title Data 가져오기
        # test = driver.find_elements_by_class_name("GameScheduleList_title__2fTpK")

        # for i in test:
        #     print(i.text)


    #     doc = {
    #     'name': list_OlympicItemKor[i],
    #     'id': list_OlympicItem[i] + i,
    #     'date': 0,
    #     'time': 0,
    #     'title': 0,
    #     'matchState': 0,
    #     'entry': 0,
    #     'matchResult': 0,
    # }

    #     db.dbPlan.insert_one(doc) 
        # print('완료!')


# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
    db.dbPlan.drop()  # mystar 콜렉션을 모두 지워줍니다.

### 실행하기
insert_all()
init_items()
