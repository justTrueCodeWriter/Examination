from flask import Flask, render_template, request
from src.database_operations import getDataFromDatabase, getAmountOfCorrectAnswers

app = Flask(__name__)

test_result = 0
questions_count = 0

def checkTestResult(answers, isTestFinished: bool) -> bool:
    global test_result
    test_result = 0
    answer_id = 1
    for answer in answers:
        if (request.args.get(f"choice_box_element{answer_id}")):
            isTestFinished = True
        if (request.args.get(f"choice_box_element{answer_id}")=='1'):
            test_result+=1
        answer_id += 1
    return isTestFinished

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
    global questios_count
    max_score = getAmountOfCorrectAnswers(answers) 
    isTestFinished = checkTestResult(answers, isTestFinished)

    return render_template("test.html", questions=questions, answers=answers, isTestFinished=isTestFinished, test_result=test_result, max_score=max_score) 

@app.route('/test2')
def test2():
    isTestFinished = False
    questions, answers = getDataFromDatabase(2) 
    global questios_count
    max_score = getAmountOfCorrectAnswers(answers) 
    isTestFinished = checkTestResult(answers, isTestFinished)

    return render_template("test.html", questions=questions, answers=answers, isTestFinished=isTestFinished, test_result=test_result, max_score=max_score) 

@app.route('/test3')
def test3():
    isTestFinished = False
    questions, answers = getDataFromDatabase(3) 
    global questios_count
    max_score = getAmountOfCorrectAnswers(answers) 
    isTestFinished = checkTestResult(answers, isTestFinished)

    return render_template("test.html", questions=questions, answers=answers, isTestFinished=isTestFinished, test_result=test_result, max_score=max_score) 

@app.route('/examination')
def examination():
    questions, answers = getDataFromDatabase(4) 
    return render_template("test.html", questions=questions, answers=answers) 
