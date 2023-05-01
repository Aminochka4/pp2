import psycopg2

# 1 пункт задачи
# cur.execute("CREATE TABLE phonebook (userid SERIAL PRIMARY KEY, username text NOT NULL, phone text NOT NULL)")

def create_users(cur):
    a = input("Enter username: ")
    b = input("Enter phone: ")
    cur.execute(f"INSERT INTO phonebook (username, phone) VALUES ('{a}', '{b}')")

def insert_csv(cur, path):
    with open(path, "r") as csv:
        next(csv)
        cur.copy_from(csv, "phonebook", sep = ",")

def delete(cur):
    userid = int(input("Which one you want to delete: "))
    cur.execute(f"DELETE FROM phonebook WHERE userid = {userid}")

def change_username(cur):
    userid = int(input("Which one you want to change: "))
    username = input("New username: ")
    cur.execute(f"UPDATE phonebook SET username = '{username}' WHERE userid = {userid}")

def change_phone(cur):
    userid = int(input("Which one you want to change: "))
    phone = input("New phone: ")
    cur.execute(f"UPDATE phonebook SET phone = '{phone}' WHERE userid = {userid}")

def get_number_by_username(cur):
    username = input("Whose number you want: ")
    cur.execute(f"SELECT phone FROM phonebook WHERE username = '{username}'")
    result = cur.fetchone()
    print(result[0])

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Idinahui12345")

cur = conn.cursor()
# 2 пункт задачи
# create_users(cur)
# path = r"C:\pp2\all labs\phonebook.csv"
# insert_csv(cur, path)

# 4 пункт задачи(выводит номер по веденному юзернейму)
# get_number_by_username(cur)


# 3 пункт задачи
# change_phone(cur)
# change_username(cur)

# 5 пункт задачи
# delete(cur)

# выводит всю таблицу
# ORDER BY означает сортировку по возрастанию айди
cur.execute("SELECT * FROM phonebook ORDER BY userid")
results = cur.fetchall()
for i in results:
    print(i)

conn.commit()
cur.close()
conn.close()
