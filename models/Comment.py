from app import *
import datetime

class Comment():

    def __init__(self,comment=None,user=None, post=None):
        self.comment = comment
        self.user = user
        self.post = post

    def writeComment(self):
        fecha = datetime.datetime.now()
        cursor.execute("INSERT INTO comments (comment, user_id, blog_id) VALUES (?,?,?)",(self.comment, self.user, self.post))
        db.commit()
        return [cursor.rowcount,self]

    def query(self):
        cursor.execute(f"SELECT * FROM comments WHERE blog_id = {self.post} ")
        result = cursor.fetchall()

        users = []
        for user in result:
            cursor.execute(f"SELECT * FROM users WHERE id = {user[2]} ")
            u = cursor.fetchone()
            users.append(u)

        return [result,users]

    def _findBlogID(self):
        cursor.execute("SELECT id FROM posts WHERE title = ?",(self.blogtitle,))
        result = cursor.fetchone()
        return result[0]