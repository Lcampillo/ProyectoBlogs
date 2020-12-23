from app import *
import datetime

class Blog():

    def __init__(self,title=None,description=None,published=None,state=None,image=None):
        self.title = title
        self.description = description
        self.published = published
        self.state = state
        self.image = image

    def query(self):
        cursor.execute("SELECT * FROM posts")
        result = cursor.fetchall()
        return result
    
    def store(self):
        fecha = datetime.datetime.now()
        cursor.execute("INSERT INTO posts (user_id,title,description,published,state,image,created_at) VALUES(?,?,?,?,?,?,?)",(session["id"],self.title,self.description,self.published,self.state,self.image,fecha))
        db.commit()
        return [cursor.rowcount,self]
    
    def search(self):
        cursor.execute(f"SELECT * FROM posts WHERE title like '%{self.title}%' ")
        result = cursor.fetchall()

        return result