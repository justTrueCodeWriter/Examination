from flask import Flask, render_template, request
from src.database_operations import getDataFromDatabase, getAmountOfCorrectAnswers

app = Flask(__name__)

test_result = 0
questions_count = 0

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/theory')
def theory():
    return render_template("theory.html")

@app.route('/test1')
def test1():
    isTestFinished = False
    questions, answers = getDataFromDatabase(1) 
    global test_result
    global questios_count
    test_result = 0
    max_score = getAmountOfCorrectAnswers(answers) 
    answer_id = 1
    for answer in answers:
        if (request.args.get(f"choice_box_element{answer_id}")):
            isTestFinished = True
        if ((bool(answer[2])==True) and (request.args.get(f"choice_box_element{answer_id}")==str(answer[2]))):
            test_result+=1
        answer_id += 1

    print(test_result)
    return render_template("test.html", questions=questions, answers=answers, isTestFinished=isTestFinished, test_result=test_result, max_score=max_score) 

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
