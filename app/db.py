import sqlite3


def AppDb() -> sqlite3.Connection:
    conn = sqlite3.connect('wireguard.db')
    return conn
