import sqlite3

conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()


quary ="""
create table tests (
id integer primary key autoincerement,
quastion TEXT,
answer_1,
answer_2,
answer_3,
answer_4,
right_answer TEXT,
chat_id INTEGER
)
"""
cursor.execute(quary)
conn.commit()