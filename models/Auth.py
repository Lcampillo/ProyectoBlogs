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
        crypted = hashlib.sha256()
        crypted.update(self.password.encode("utf-8"))

        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ? ",(self.email,crypted.hexdigest()))
        result = cursor.fetchone()
        return result

    def register(self):
        fecha = datetime.datetime.now()
        activation_key = self.generate_key()
        crypted = hashlib.sha256()
        crypted.update(self.password.encode("utf-8"))

        cursor.execute("INSERT OR IGNORE INTO users (name, surname, password, rol, contact, email, hash ,activated, created_at) VALUES ( ?, ? ,? ,? ,? ,?, ?, ? , ?)",
                        (self.name, self.surname, crypted.hexdigest() , 'user', self.contact, self.email, activation_key ,'false', fecha))
        db.commit()

        return [cursor.rowcount,self,'success',activation_key]

    def update(self):
        for idx, account  in enumerate(db):       
            if self.email in account[0]:
                account = (self.email,self.newPassword)
                db[idx] = account
                return 'success'

    def generate_key(self):
        longitud = 18
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=@#%+"

        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        return p

