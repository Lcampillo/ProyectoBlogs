from app import *
import datetime
from random import choice
import hashlib

class Auth():

    def __init__(self, name = None, surname = None, email= None, contact = None, password = None, newPassword = None):
        self.name = name
        self.surname = surname
        self.email = email
        self.contact = contact
        self.password = password
        self.newPassword = newPassword

    def login(self):
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ? ",(self.email,self._encrypt(self.password)))
        result = cursor.fetchone()
        return result

    def register(self):
        fecha = datetime.datetime.now()
        activation_key = self.generate_key()

        cursor.execute("INSERT OR IGNORE INTO users (name, surname, password, rol, contact, email, hash ,activated, created_at) VALUES ( ?, ? ,? ,? ,? ,?, ?, ? , ?)",
                        (self.name, self.surname, self._encrypt(self.password) , 'user', self.contact, self.email, activation_key ,'false', fecha))
        db.commit()

        return [cursor.rowcount,self,'success',activation_key]

    def update(self):
        try:
            cursor.execute("UPDATE users SET password = ?, name = ?, surname = ?, contact = ?  WHERE email = ?",
            (self._encrypt(self.newPassword), self.name, self.surname, self.contact, self.email))
            db.commit()
            return 'success'
        except:
            return 'something went wrong'

    def generate_key(self):
        longitud = 18
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=@#%+"

        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        return p

    def _encrypt(self,password):
        crypted = hashlib.sha256()
        crypted.update(password.encode("utf-8"))
        return crypted.hexdigest()

