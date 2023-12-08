from flask import Flask, render_template
from src.exam_functions import getDataFromDatabase
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/theory')
def theory():
    return render_template("theory.html")

@app.route('/test1')
def test1():
    questions = getDataFromDatabase() 
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
