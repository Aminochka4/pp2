import psycopg2
from connection import conn

# cur.execute("CREATE TABLE phonebook2 (userid SERIAL PRIMARY KEY, username varchar(255) NOT NULL, Phone varchar(255) NOT NULL)")


def create_users(cur):
    a = input("Enter username: ")
    b = input("Enter phone: ")
    cur.execute(f"INSERT INTO phonebook2 (username, phone) VALUES ('{a}', '{b}')")

# 1 задача
# for looking for users with certain pattern
def sort_by_pattern(cur):
    cur.execute("SELECT username FROM phonebook2 WHERE Phone LIKE '8705%' OR Phone LIKE '+7705%';")
    result = cur.fetchall()
    print("Beeline users: ")
    for i in result:
        print(i[0])

# 2 задача
# for adding new number or changing number if username already exists
def add_or_update(cur):
    username = input("Enter username: ")
    cur.execute(f"SELECT userid FROM phonebook2 WHERE username = '{username}'")
    result = cur.fetchone()
    if result:
        phone = input("User already exists, but you can update: ")
        while True:
            if (phone[:2] == '87' and len(phone) == 11) or (phone[:3] == '+77' and len(phone) == 12):
                return False
            else:
                phone = input("Incorrect form of phone, try again: ")
        cur.execute(f"UPDATE phonebook2 SET phone = '{phone}' WHERE username = '{username}'")
    else:
        phone = input("Enter phone number: ")
        while True:
            if (phone[:2] == '87' and len(phone) == 11) or (phone[:3] == '+77' and len(phone) == 12):
                return False
            else:
                phone = input("Incorrect form of phone, try again: ")
        cur.execute(f"INSERT INTO phonebook2 (username, phone) VALUES ('{username}', '{phone}')")

# 3 задача
def list_adding(cur, list):
    incorrect = []
    for i in list:
        if (i[1][:2] == '87' and len(i[1]) == 11) or (i[1][:3] == '+77' and len(i[1]) == 12):
            cur.execute(f"INSERT INTO phonebook2 (username, phone) VALUES ('{i[0]}', '{i[1]}')")
        else:
            incorrect.append(i)
    return incorrect

# 4 задача
def pagination(cur, page_num, page_size):
    offset = (page_num - 1) * page_size
    limit = page_size
    cur.execute(f"SELECT * FROM phonebook2 ORDER BY userid OFFSET {offset} LIMIT {limit}")
    rows = cur.fetchall()
    for i in rows:
        print("User id: " + str(i[0]) + ", Username: " + i[1] + ", Phone: " + i[2])

# 5 задача
def delete(cur):
    choice = input("How do you want to delete information(by username or phone)? Select only one: ")
    if choice == "username":
        username = input("Enter username: ")
        cur.execute(f"DELETE FROM phonebook2 WHERE username = '{username}'")
    elif choice == "phone":
        phone = input("Enter phone: ")
        cur.execute(f"DELETE FROM phonebook2 WHERE phone = '{phone}'")
    else:
        print("It is not correct choice")


list = [('Ernar', '+77096578976'), ('Danabek', '8706876908976'), ('Nurbek', '87476579875')]

cur = conn.cursor()

# incorrect = list_adding(cur, list)
# print(incorrect)
# add_or_update(cur)
# pagination(cur, 2, 4)
# delete(cur)

conn.commit()
cur.close()
conn.close()
