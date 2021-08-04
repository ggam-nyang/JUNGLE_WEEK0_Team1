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
# driver.implicitly_wait(5)

list_OlympicItem = ["KTE", "GLF", "MPN", "BSK", "RUG", "WRE", "VOL", "BDM", "BOX", "SHO", "CYC", "SRF", "AQU", "SKB", "CLB", "EQU",
 "BSB", "ARC", "WLF", "SAL", "JUD", "ATH", "ROW", "GYM", "FBL", "CAS", "TTE", "TKW", "TEN", "TRI", "FEN", "HOC", "HBL"]

list_OlympicItemKor = ["가라테", "골프", "근대5종", "농구", "럭비", "레슬링", "배구", "배드민턴", "복싱", "사격", "사이클", "서핑", "수영", "스케이딩 보딩", "스포츠 클라이밍", "승마",
 "야구 / 소프트볼", "양궁", "역도", "요트", "유도", "육상", "조정", "체조", "축구", "카누", "탁구", "태권도", "테니스", "트라이애슬론", "펜싱", "하키", "핸드볼"]




# DB에 저장할 경기 일정의 출처 url을 가져옵니다.
def init_items():

    # for i in range(len(list_OlympicItem)):
        
        driver.get('https://m.sports.naver.com/tokyo2020/schedule/index?type=discipline&date=&disciplineId=' + list_OlympicItem[9] + '&isKorean=Y')
        driver.implicitly_wait(5)
        
        # soup = BeautifulSoup(driver.page_source, 'html.parser')


        # matchResult Data 가져오기

        # test = driver.find_elements_by_class_name("GameScheduleList_status__3zxOL")
        
        # for i in test:
        #     # print(i.text) # 해당 텍스트를 가져옴
        #     print(i.tag_name) # 해당 태그를 가져옴
            


        # Time Data 가져오기
        # test = driver.find_elements_by_class_name("GameScheduleList_game_time__10dNy")

        # for i in test:
        #     print(i.text)


        # entry Data 가져오기
        # test = driver.find_elements_by_class_name("GameScheduleList_link_name__xBm7W")

        # for i in test:
        #     print(i.text)

        # # date Data 가져오기
        # dates = driver.find_elements_by_class_name("Schedule_date__iFiUq")

        # for date in dates:
        #     # print(date.text)


        # Title Data 가져오기
        # test = driver.find_elements_by_class_name("GameScheduleList_title__2fTpK")

        # for i in test:
        #     print(i.text)



        # test Data 가져오기
        divs = driver.find_elements_by_class_name("Schedule_game_schedule__1k6hJ")
        # test = driver.find_elements_by_class_name("GameScheduleList_game_schedule_list__21Umh")

        # testHtml = test[0].get_attribute('innerHTML')
        # print(testHtml)


########################### 로직 시작 #######################################
        for i in range(len(divs)):
            divHtml = divs[i].get_attribute('innerHTML')
            # print(type(divHtml))

            soup = BeautifulSoup(divHtml, 'html.parser')

            dates = driver.find_elements_by_class_name("Schedule_date__iFiUq")
            print(dates[i].text)

            times = soup.select('.GameScheduleList_game_time__10dNy')
            titles = soup.select('.GameScheduleList_title__2fTpK')
            matchStates = soup.select('span.GameScheduleList_status__3zxOL')
            matchResults = soup.select('.GameScheduleList_player_list__1ll9D')


            for i in range(len(times)):
                print(times[i].text)
                print(titles[i].text)
                print(matchStates[i].text)
                
                ulHtml = matchResults[i]
                soupResult = BeautifulSoup(ulHtml.text, 'html.parser')
                entrys = soupResult.select_one('.GameScheduleList_link_name__xBm7W').text
                print(entrys)




                # print(type(entrys))

                # entrys = soupResult.select('div.GameScheduleList_player_inner__31liD > .GameScheduleList_link_name__xBm7W')
                # print(entrys)
                # Results = soupResult.select('.GameScheduleList_status__3zxOL')
                # # print(Results)

                # list_entry = []
                # list_result = []

                # for entry in entrys:
                #     list_entry.append(entry)
                # for result in Results:
                #     list_result.append(result)
                
                # print(list_entry)
                # print(list_result)

                







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

