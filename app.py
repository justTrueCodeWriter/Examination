from flask import Flask, render_template, request
from src.database_operations import getDataFromDatabase, getAmountOfCorrectAnswers

app = Flask(__name__)

test_result = 0
questions_count = 0
access_level = 0

def checkTestResult(answers, isTestFinished: bool) -> bool:
    global test_result
    test_result = 0
    for answer_id in range(1, len(answers)):
        if (request.args.get(f"choice_box_element{answer_id}")):
            isTestFinished = True
        if (request.args.get(f"choice_box_element{answer_id}")=='1'):
            test_result+=1
    return isTestFinished

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/theory')
def theory():
    return render_template("theory.html")

@app.route('/test1')
def test1():
    test_level = 1

    isTestFinished = False
    questions, answers = getDataFromDatabase(test_level) 
    global questios_count
    global access_level
    max_score = getAmountOfCorrectAnswers(answers) 
    isTestFinished = checkTestResult(answers, isTestFinished)
    if (isTestFinished):
        access_level+=1

    return render_template("test.html", questions=questions, answers=answers, isTestFinished=isTestFinished, test_result=test_result, max_score=max_score) 

@app.route('/test2')
def test2():
    test_level = 2

    isTestFinished = False
    questions, answers = getDataFromDatabase(test_level) 
    global questios_count
    global access_level
    max_score = getAmountOfCorrectAnswers(answers) 
    isTestFinished = checkTestResult(answers, isTestFinished)
    if (isTestFinished):
        access_level+=1

    if (access_level >= test_level-1):
        return render_template("test.html", questions=questions, answers=answers, isTestFinished=isTestFinished, test_result=test_result, max_score=max_score) 
    else:
        message = "У вас нет доступа к этому тесту. Завершите предыдущий тест."
        return render_template("message_page.html", message=message) 

@app.route('/test3')
def test3():
    test_level = 3

    isTestFinished = False
    questions, answers = getDataFromDatabase(test_level) 
    global questios_count
    global access_level
    max_score = getAmountOfCorrectAnswers(answers) 
    isTestFinished = checkTestResult(answers, isTestFinished)
    if (isTestFinished):
        access_level+=1

    if (access_level >= test_level-1):
        return render_template("test.html", questions=questions, answers=answers, isTestFinished=isTestFinished, test_result=test_result, max_score=max_score) 
    else:
        message = "У вас нет доступа к этому тесту. Завершите предыдущий тест."
        return render_template("message_page.html", message=message) 
