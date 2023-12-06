from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/test1')
def test1():
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor();
    cursor.execute("select * from questions");
    questions = cursor.fetchall()
    connect.close();
    return render_template("test.html", questions=questions) 

@app.route('/test2')
def test2():
    return render_template("test.html"); 

@app.route('/test3')
def test3():
    return render_template("test.html"); 

@app.route('/examination')
def examination():
    return render_template("test.html"); 
