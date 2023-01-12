import sqlite3
from tqdm import tqdm

conn = sqlite3.connect('new_data.sql')
cursor = conn.cursor()
todo = []
for row in tqdm(open('data-dump.sql', mode="r", encoding="utf8", errors="ignore")):
    if not row.startswith('--'):
        todo.append(row)
new_todo = "".join(todo).replace("\n", "").replace("`", '"').replace("''", "").split(";")
open("out.txt", mode="w", errors="ignore").writelines(new_todo)

for row in tqdm(new_todo):
    try:
        cursor.execute(row)
    except Exception as e:
        print(row)
        print(e)
        break

print(cursor.fetchone()[0])
