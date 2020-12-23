from app import *
import datetime

class Comment():

    def __init__(self,body=None,user=None, blogtitle=None):
        self.body = body
        self.user = user
        self.blogtitle = blogtitle

    def writeComment(self):
        self.created_at = datetime.datetime.now()
        cursor.execute("INSERT INTO comments (comment, user_id, blog_id) VALUES (?,?,?)",(self.body, session["id"], self._findBlogID(self.blogtitle)))
        db.commit()
        return [cursor.rowcount,self]
        # TODO agregar columna created_at

    def _findBlogID(self):
        cursor.execute("SELECT id FROM posts WHERE title = ?",(self.blogtitle,))
        result = cursor.fetchone()
        return result[0]