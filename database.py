import sqlite3 as sq
from datetime import datetime
import time



def create_db():
    con = sq.connect('base.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS seeds(
        address TEXT,
        privatekey TEXT
    )""")
    con.commit()
    print('-----------------------------\nDatabase created')
    create_index_address()
    create_index_privatekey()

def create_index_address():
    con = sq.connect('base.db')
    cur = con.cursor()
    cur.execute("""CREATE INDEX IF NOT EXISTS address_idx ON seeds (address)""")
    con.commit()
    print('-----------------------------\nIndex address created')
    
def create_index_privatekey():
    con = sq.connect('base.db')
    cur = con.cursor()
    cur.execute("""CREATE INDEX IF NOT EXISTS privatekey_idx ON seeds (privatekey)""")
    con.commit()
    print('-----------------------------\nIndex privatekey created')    
#Check addresses in base
def check(info):
    con = sq.connect('base.db')
    cur = con.cursor()
    cur.execute("PRAGMA journal_mode = OFF")
    cur.execute(f"SELECT address FROM seeds WHERE address = ?", (info[0], ))
    data = cur.fetchone()
    if data is None:
        cur.execute("INSERT INTO seeds VALUES(?,?)", (info[0], info[1]))
        con.commit()
        return True
    else:
        con.commit()
        return False
#Check addresses from block
def search_addr(address):
    con = sq.connect('base.db')
    cur = con.cursor()
    cur.execute("PRAGMA journal_mode = OFF")
    cur.execute(f"SELECT address FROM seeds WHERE address = ?", [address])
    data = cur.fetchone()
    con.commit()
    if data is None:
        return False
    else:
        return True

def get_pk_address(address):
    con = sq.connect('base.db')
    cur = con.cursor()
    cur.execute("PRAGMA journal_mode = OFF")
    cur.execute("SELECT privatekey FROM seeds WHERE address = ?", [address])
    data = cur.fetchone()[0]
    con.commit()
    return data
    