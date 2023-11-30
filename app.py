from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/test1')
def test1():
    return "<h1>TEST1</h1>" 

@app.route('/test2')
def test2():
    return "<h1>TEST2</h1>" 

@app.route('/test3')
def test3():
    return "<h1>TEST3</h1>" 

@app.route('/examination')
def examination():
    return "<h1>EXAMINATION</h1>" 
