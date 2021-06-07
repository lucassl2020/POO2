import sqlite3

conexao = sqlite3.connect("testDB.sqlite")
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(
            id integer PRIMARY KEY,
            nome text NOT NULL,
            email text NOT NULL
        );"""

nome = "lucas"
email = "lucaslopes@gmail.com"

cursor.execute(sql)
for i in range(5):
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?,?)", (nome, email))

cursor.execute("SELECT * from usuarios")

for c in cursor:
    print(c)

conexao.commit()
conexao.close()
