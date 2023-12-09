import sqlite3

def getDataFromDatabase(): 
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor();
    cursor.execute("select * from questions");
    data = cursor.fetchall()
    connect.close();
    return data

def getTheory():
    file = open("theory.md", "r")   
    data = file.read()
    file.close()
    return data
