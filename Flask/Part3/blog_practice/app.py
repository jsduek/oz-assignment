from flask import Flask
from flask_smorest import Api
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db_info = yaml.load(open('db.yaml'), Loade=yaml.Fullloader)
app.config['MYSQL_HOST'] = db_info['mysql_host']
app.config['MYSQL_USER'] = db_info['mysql_user']
app.config['MYSQL_PASSWORD'] = db_info['mysql_password']
app.config['MYSQL_DB'] = db_info['mysql_db']

mysql = MySQL(app)

# blueprint 설정
app.configp['API_TITLE'] = 'Blog API List'
app.configp['API_VERSION'] = '1.0'
app.configp['OPENAPI_VERSION'] = '3.1.3'
app.configp['OPENAPI_URL_PREFIX'] = '/'
app.configp['OPENAPI_SWQGGER_UI_PATH'] = '/swagger-ui'
app.configp['OPENAPI_SWQGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

from flask import render_template
@app.route('/blogs')
def manage_blogs():
    return render_template("posts.html")

if __name__ == '__main__':
    app.run(debug=True)