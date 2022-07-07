import sqlite3


class Database:

    def __init__(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
        conn.commit()
        conn.close()

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",
                    (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=?OR author=?OR year=?OR isbn=?",
                    (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=?WHERE id=?",
                    (title, author, year, isbn, id))
        conn.commit()
        conn.close()


# insert("the Banana", "Wa Na", 1983, 30880)
# delete(3)
#update(4, "the sun", "Wa Yi", 1962, 308798)
# print(view())
#print(search(author="Wa Di"))
