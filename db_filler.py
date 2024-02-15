import sys
import sqlite3

def push_question(connect: sqlite3.Connection, cursor: sqlite3.Cursor) -> int:
    print("question: ", end='')
    question = str(input())
    if (question=="exit"):
        return 0
    cursor.execute(f"insert into questions (question, difficulty_level) values ('{question}', {sys.argv[2]})")
    connect.commit()
    return 1

def push_answer(connect: sqlite3.Connection, cursor: sqlite3.Cursor) -> int:
    print("question_id: ", end='')
    question_id = int(input())
    print("answer: ", end='')
    answer = str(input())
    if (answer=="exit"):
        return 0 
    print("is_correct: ", end='')
    is_correct = int(input())
    cursor.execute(f"insert into answers (question_id, answer, is_correct, difficulty_level) values ({question_id}, '{answer}', {is_correct}, {sys.argv[2]})")
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
else:
    print("INCORRECT! Execute without required arguments!");
