import sqlite3

def view_backpack(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM contents")
    list = cur.fetchall()
    print(list)
    return list

def add_backpack(db, item_name, item_description):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    query = "INSERT INTO contents(name, description) VALUES (?,?) "
    cur.execute(query,(item_name, item_description))
    conn.commit()

def delete_backpack(db, item_name):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    query = "DELETE FROM contents WHERE name = ?"
    cur.execute(query, item_name)
    conn.commit()

def edit_backpack(db, item_name, new_item_name, new_item_description):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

def clear_backpack(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("DELETE FROM contents")
    conn.commit()
