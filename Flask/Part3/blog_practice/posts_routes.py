from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description='posts api', url_prefix='/')

    @posts_blp.route('/', methods=['GET', 'POST'])
    def posts():
        cursor = mysql.connection.cursor()
        # 게시글 조회
        if request.method == 'GET':
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            post_list = []

            for post in posts:
                post_list.append({
                    'id': post[0],
                    'title': post[1],
                    'content': post[2]
                })

            return jsonify(post_list)
        
        # 게시글 생성
        elif request.method == 'POST':
            title = request.json.get('title')
            content = request.json/get('content')

            if not title or not content:
                abort(400. message="Title or Content cannot be empty")

            sql = 'INSERT INTO posts(title, contet) VALUES(%s, %s)'
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            return jsonify({'msg':"successfully created post data", "title":title, "content":content}), 201
        

    # 1번 게시글만 조회하고 싶은 경우
    # 게시글 수정 및 삭제

    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def posts(id):
        cursor = mysql.connection.cursor()

        if request.method == 'GET':
            sql = "SELECT * FROM posts WHERE id = {id}"
            cursor.execute(sql)
            post = cursor.fechone()

            if not post:
                abort(404, "Not found post")
            return ({'id': post[0],
                    'title': post[1],
                    'content': post[2]
                    })
        elif request.method == 'PUT':
            # data = request.json
            # title = data['title']  -  아래의 코드와 같다

            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, "Not found title, content")

            sql = f"UPDATE posts SET title={title}, content={content} WHERE id ={id}"
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({"msg":"Successfully updated title % content"})

        elif request.method == 'DELETE':
            if not post:
                abort(400, "Not found title, content")
                
            sql = f"DELETE FROM posts WHERE id={id}"
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({"msg":"Successfully  deleted title & content"})
