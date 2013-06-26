import web
import datetime

db = web.database(dbn='mysql', db='blog', user='root', pw='root')

def get_posts():
    return db.select('entries', order='id DESC')

def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, content):
    db.insert('entries', title=title, content=content, posted_on=datetime.datetime.utcnow())

def del_post(id):
    db.delete('entries', where='id=$id', vars=locals())

def update_post(id, title, content):
    db.update('entries', where='id=$id', vals=locals(), title=title, content=conetent)
