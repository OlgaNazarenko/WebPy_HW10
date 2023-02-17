import sqlite3
import configparser
import os
from pathlib import Path

from mongoengine import connect

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, 'config.ini')

# Connect to MongoDB database
config = configparser.ConfigParser()
config.read('config.ini')

m_user = config.get('DB', 'user')
m_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

conn = connect(host = f"mongodb+srv://{m_user}:{m_pass}@{domain}/{db_name}?retryWrites=true&w=majority")

authors = conn.db[db_name].authors.find()
quotes = conn.db[db_name].quotes.find()


# Connect to SQLite database
conn = sqlite3.connect("web8.db")
cursor = conn.cursor()

# Create a table in SQLite
cursor.execute('''CREATE TABLE IF NOT EXISTS author (
                 id INTEGER PRIMARY KEY,
                 fullname TEXT,
                 born_date DATE,
                 born_location TEXT,
                 description TEXT
             )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS quote (
                 id INTEGER PRIMARY KEY,
                 quote TEXT,
                 author TEXT
                 tags TEXT,
                 author_id INTEGER,
                 FOREIGN KEY (author_id) REFERENCES author(id)
             )''')

# Insert each a/q from MongoDB collection into SQLite table
for aut in authors:
    cursor.execute("INSERT INTO author (id, fullname, born_date, born_location, description) VALUES (?, ?, ?, ?, ?)",
                   (aut["_id"], aut["fullname"], aut["born_date"], aut["born_location"], aut["description"]))

for q in quotes:
    cursor.execute("INSERT INTO quote (id, quote, author, tags, author_id) VALUES (?, ?, ?, ?, ?)",
                   (q["_id"], q["quote"], q["author"], q["tags"], q["author_id"]))


conn.commit()
conn.close()
