import sqlite3

def getDataFromDatabaseByQuery(sql_query: str) -> list:
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute(f"{sql_query}")
    data = cursor.fetchall()
    connect.close()
    return data

def getDataFromDatabase(difficulty_level: int) -> tuple: 
    questions = getDataFromDatabaseByQuery(f"select * from questions where difficulty_level={difficulty_level}")
    answers = getDataFromDatabaseByQuery(f"select * from answers where difficulty_level={difficulty_level}")
    return questions, answers

def getAmountOfCorrectAnswers(answers: list[str]) -> int:
    counter = 0
    for answer in answers:
        if (bool(answer[2]) == True):
            counter += 1;
    return counter
