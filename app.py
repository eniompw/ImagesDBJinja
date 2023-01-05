from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def select():
    con = sqlite3.connect('shop.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM stock")
    rows = cur.fetchall()
    return render_template("index.html", list=rows)

def insert():
	con = sqlite3.connect('shop.db')
	cur = con.cursor()
	cur.execute("""	INSERT INTO stock (sid, name, image)
					VALUES ("2", "buffalo", "buffalo.jpg")
			    """)
	con.commit()
	return 'INSERT'

def create():
    con = sqlite3.connect("shop.db")
    cur = con.cursor()
    try:
        cur.execute("""
        CREATE TABLE stock(
            sid VARCHAR(30) NOT NULL PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            image VARCHAR(30) NOT NULL)
        """)
    except sqlite3.OperationalError as e:
        return str(e)
    return "table created"