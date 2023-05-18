import sqlite3

import sqlite3


def AppDb():
    conn = sqlite3.connect('wireguard.db')
    return conn
