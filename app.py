from types import MethodDescriptorType
from flask import Flask, json, render_template, jsonify, request, url_for, session, redirect
from jinja2 import Template

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbOlympic


app.secret_key = 'asfewagwalkg-wlnefwelknfew'




## HTML을 주는 부분
@app.route('/')
def home():
    list_OlympicItemKor = ["가라테", "골프", "근대5종", "농구", "럭비", "레슬링", "배구", "배드민턴", "복싱", "사격", "사이클", "서핑", "수영", "스케이딩 보딩", "스포츠 클라이밍", "승마",
 "야구 / 소프트볼", "양궁", "역도", "요트", "유도", "육상", "조정", "체조", "축구", "카누", "탁구", "태권도", "테니스", "트라이애슬론", "펜싱", "하키", "핸드볼"]
    if 'userID' in session:
        return render_template('index.html', sportlist=list_OlympicItemKor, username = session.get('userID'), login=True)
    else:
        return render_template('index.html', sportlist=list_OlympicItemKor, login=False)

## 회원가입 체크
@app.route('/join', methods=['POST'])
def joinCheck():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    if id_receive == '':
        return jsonify({'result': 'blank'})

    is_id_in_db = db.users.find_one({'id': id_receive})
    if is_id_in_db == None:
        new_user = {'id': id_receive, 'password': pw_receive, 'bookmark': []}
        db.users.insert_one(new_user)
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'same'})

## 로그인 체크
@app.route('/login', methods=['POST'])
def loginCheck():
    input_id = request.form['login_id']
    input_pw = request.form['login_pw']

    is_id_in_db = db.users.find_one({'id': input_id}, {'_id': 0})

    if is_id_in_db == None:
        return jsonify({'result': 'idError'})
    else:
        if is_id_in_db['password'] != input_pw:
            return jsonify({'result': 'pwError'})
        else:
            session["userID"] = input_id
            return jsonify({'result': 'success', 'userName': session['userID']})


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userID')
    print(session)
    return jsonify({'result': 'success'})


@app.route('/schedule', methods=['POST'])
def makeSchedule():
    item_selected = request.form['item_give']
    item_schedule = list(db.dbPlan.find({'name': item_selected}, {'_id': 0}))
    return jsonify({'result': 'success', 'schedule_give': item_schedule})

## 북마크 눌렀을 때, user db에 추가하는 기능
@app.route('/addBookmark', methods=['POST'])
def addBookmark():
    item_id = request.form['item_id_give']
    print(item_id)
    db.users.update_one(
        {'id': session['userID']},
        { '$push': { 'bookmark': item_id}}
    )

    return jsonify({'result': 'success', 'userID': session['userID']})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
