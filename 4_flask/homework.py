from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index_hw.html')


## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def order_post():
    name_receive = request.form['name_give']
    select_receive = request.form['select_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    order = {
        'name': name_receive,
        'select': select_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.oredrs.insert_one(order)

    return jsonify({'result': 'success', 'msg': '주문내용이 저장되었습니다.'})


@app.route('/orders', methods=['GET'])
def order_get():
    orders = list(db.reviews.find({},{'_id':0}))
    # name_receive = request.args.get('name_give')
    # select_receive = request.args.get('select_give')
    # address_receive = request.args.get('address_give')
    # phone_receive = request.args.get('phone_give')


    return jsonify({'result': 'success', 'msg': '주문목록을 가져옵니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
