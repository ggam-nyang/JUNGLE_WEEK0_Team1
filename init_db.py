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
# /home/ubuntu/jungle/chromedriver_linux64/chromedriver
driver = webdriver.Chrome('C:\Users\이재윤\Desktop\WEEK0_Team1/chromedriver', options=options)

list_OlympicItem = ["KTE", "GLF", "MPN", "BSK", "RUG", "WRE", "VOL", "BDM", "BOX", "SHO", "CYC", "SRF", "AQU", "SKB", "CLB", "EQU",
 "BSB", "ARC", "WLF", "SAL", "JUD", "ATH", "ROW", "GYM", "FBL", "CAS", "TTE", "TKW", "TEN", "TRI", "FEN", "HOC", "HBL"]

list_OlympicItemKor = ["가라테", "골프", "근대5종", "농구", "럭비", "레슬링", "배구", "배드민턴", "복싱", "사격", "사이클", "서핑", "수영", "스케이딩 보딩", "스포츠 클라이밍", "승마",
 "야구 / 소프트볼", "양궁", "역도", "요트", "유도", "육상", "조정", "체조", "축구", "카누", "탁구", "태권도", "테니스", "트라이애슬론", "펜싱", "하키", "핸드볼"]




########################### 로직 시작 #######################################

def init_items():

    for i in range(len(list_OlympicItem)):
        id_index = 0

        driver.get('https://m.sports.naver.com/tokyo2020/schedule/index?type=discipline&date=&disciplineId=' + list_OlympicItem[i] + '&isKorean=Y')
        driver.implicitly_wait(2)

        divs = driver.find_elements_by_class_name("Schedule_game_schedule__1k6hJ")

        if divs == []:
            print("데이터가 없습니다")
            continue
            


        for j in range(len(divs)):
            divHtml = divs[j].get_attribute('innerHTML')

            soup = BeautifulSoup(divHtml, 'html.parser')

            dates = driver.find_elements_by_class_name("Schedule_date__iFiUq")
            print(dates[j].text)

            times = soup.select('.GameScheduleList_game_time__10dNy')
            titles = soup.select('.GameScheduleList_title__2fTpK')
            matchStates = soup.select('span.GameScheduleList_status__3zxOL')
            matchResults = soup.select('.GameScheduleList_player_list__1ll9D')


            for k in range(len(times)):
                print(times[k].text)
                print(titles[k].text)
                print(matchStates[k].text)

                ulHtml = str(matchResults[k])

                soupResult = BeautifulSoup(ulHtml, 'html.parser')

                entrys = soupResult.select('.GameScheduleList_link_name__xBm7W')

                Results = soupResult.select('.GameScheduleList_status__3zxOL')

                list_entry = []
                list_result = []

                for entry in entrys:
                    list_entry.append(entry.text)
                for result in Results:
                    list_result.append(result.text)

                print(list_entry)
                print(list_result)

                doc = {
        'name': list_OlympicItemKor[i],
        'id': list_OlympicItem[i] + str(id_index),
        'date': dates[j].text,
        'time': times[k].text,
        'title': titles[k].text,
        'matchState': matchStates[k].text,
        'entry': list_entry,
        'matchResult': list_result,
    }

                db.dbPlan.insert_one(doc)
                id_index += 1


def insert_all():
    db.dbPlan.drop()


# insert_all()
# init_items()

