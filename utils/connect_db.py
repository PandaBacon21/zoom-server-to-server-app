import sqlite3

#specify your database path. Using SQLite so I just created a new database folder that my SQLite database file will live 
def connect_db():
    con = sqlite3.connect('/Users/josh/Desktop/coding/new_zoom_testing/zoom_sts_oauth_app/database/sts_app.db')
    cur = con.cursor()
    # create the tokens table
    cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name = 'tokens' '''
    )
    if cur.fetchone()[0] == 1:
        print('Token Table Exists')
    else: 
        print('Tokens Table Does NOT Exist. Creating Table')
        cur.execute('CREATE TABLE tokens(uuid INTEGER UNIQUE, token TEXT, expire TEXT)')
    
    # "../database/sts_app.db"