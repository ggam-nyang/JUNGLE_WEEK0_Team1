from flask import Flask, json, render_template, jsonify, request
from jinja2 import Template

app = Flask(__name__)

import requests
##as
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbOlympic

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## 회원가입 체크
@app.route('/join', methods=['POST'])
def joinCheck():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    if id_receive == '':
        return jsonify({'result': 'blank'})

    is_id_in_db = db.users.find_one({'id': id_receive})
    if is_id_in_db == None:
        new_user = {'id': id_receive, 'password': pw_receive}
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
            return jsonify({'result': 'success', 'userName': input_id})


@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!'})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
		# 2. meta tag를 스크래핑하기
		# 3. mongoDB에 데이터 넣기
    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
