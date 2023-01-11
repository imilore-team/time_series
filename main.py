import sqlite3

conn = sqlite3.connect('new_data.sql')
cursor = conn.cursor()
todo = []
for row in open('data-dump.sql', mode="r"):
    if not row.startswith('--'):
        todo.append(row)
new_todo = "".join(todo).replace("\n", "").split(";")
open("out.txt").writelines(new_todo)

for row in new_todo:
    cursor.execute(row)

print(cursor.fetchone()[0])
