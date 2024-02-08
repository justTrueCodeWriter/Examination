import sys
import sqlite3

def push_question(connect: sqlite3.Connection, cursor: sqlite3.Cursor) -> int:
    print("question: ", end='')
    question = str(input())
    if (question=="exit"):
        return 0
    print("correct_answer_number: ", end='')
    correct_answer_number = int(input())
    #print("difficulty_level: ", end='')
    #difficulty_level = int(input())
    cursor.execute(f"insert into questions (question, correct_answer_number, difficulty_level) values ('{question}', {correct_answer_number}, {sys.argv[2]})")
    connect.commit()
    return 1

def push_answer(connect: sqlite3.Connection, cursor: sqlite3.Cursor) -> int:
    print("question_id: ", end='')
    question_id = int(input())
    print("answer: ", end='')
    answer = str(input())
    if (answer=="exit"):
        return 0 
    print("answer_number: ", end='')
    answer_number = int(input())
    #print("difficulty_level: ", end='')
    #difficulty_level = int(input())
    cursor.execute(f"insert into answers (question_id, answer, answer_number, difficulty_level) values ({question_id}, '{answer}', {answer_number}, {sys.argv[2]})")
    connect.commit()
    return 1

if (sys.argv[1]=='questions'):
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    isWorking = 1
    while (isWorking != 0):
        isWorking = push_question(connect, cursor)
    connect.close()
elif (sys.argv[1]=='answers'):
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    isWorking = 1
    while (isWorking != 0):
        isWorking = push_answer(connect, cursor)
    connect.close()
