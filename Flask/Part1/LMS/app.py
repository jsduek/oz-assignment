from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index2():
    users = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]   
    return render_template('index2.html', users=users)

if __name__ == "__name__":
    app.run(debug=True)