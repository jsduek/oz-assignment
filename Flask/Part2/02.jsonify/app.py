from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# GET
# (1) 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods = ['GET'])
def show_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}
    return jsonify(data)

# (2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result':'success', 'data':{'feed1':'data1'}}
    return jsonify(data)

# POST
# (1) 게시글을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result':'success'})

datas = [{"items": {"name": "item1", "price": 10}}]

app.route("/api/v1/datas", methods = ['GET'])
def get_datas():
    return {'datas':datas}

@app.route("/api/v1/datas", methods = ['POST'])
def create_data():
    request_data = request.get_json() # 들어오는 데이터를 json으로 받는다
    new_data = {'items': request_data.get("items", [])}
    datas.append(new_data)
    return new_data, 201

if __name__ == "__main__":
    app.run(debug=True)