from flask import Flask, render_template, request
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
    questions, answers = getDataFromDatabase(1) 
    counter = 0
    for question in questions:
        if (request.args.get(f"choice_box_element{question[0]}")==str(question[2])):
            counter+=1
    print(counter)
    return render_template("test.html", questions=questions, answers=answers) 

@app.route('/test2')
def test2():
    questions, answers = getDataFromDatabase(2) 
    return render_template("test.html", questions=questions, answers=answers) 

@app.route('/test3')
def test3():
    questions, answers = getDataFromDatabase(3) 
    return render_template("test.html", questions=questions, answers=answers) 

@app.route('/examination')
def examination():
    questions, answers = getDataFromDatabase(4) 
    return render_template("test.html", questions=questions, answers=answers) 
