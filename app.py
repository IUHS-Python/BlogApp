import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    return post

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/home')
def index():
    list_example = ["Alvin", "Simon", "Theodore"]
    return render_template("index4.html", list_example = list_example)
   # return render_template('index3.html')

@app.route('/blog')
def renderer():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run()
