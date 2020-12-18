import sqlite3
conn = sqlite3.connect('Bloggi.db')
cur = conn.cursor()
      #      cur.execute('INSERT INTO Users (name, surname, contact, email, activated) VALUES (?, ?, ?, ?, False)', (name, surname, contact, email))
    #        cur.execute('///TE Counts SET count = count + 1 WHERE org = ?', (org, ))
   # sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10
#    cur.close()

class Basededatos():

    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(self.name)
        self.cur = self.conn.cursor()

    def create_user(self, email, name, surname, contact):
        # Buscar si el email ya existe
        self.cur.execute('SELECT email FROM Users WHERE email = ?', (email, ))
        row = self.cur.fetchone()

        # No existe el email en la base de datos
        if row is None:
            self.cur.execute('INSERT INTO Users (name, surname, contact, email, activated) VALUES (?, ?, ?, ?, False)', (name, surname, contact, email))
        else:
            #cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))
            mensaje = 'El correco electronico ya existe, por favor, intente otro'
            return False, mensaje

    def update_user(self, name, surname, contact, email):
        # Buscar por mail del usurio
        self.cur.execute('SELECT email FROM Users WHERE email = ?', (email, ))
        row = self.cur.fetchone()

        self.cur.execute('UPDATE User SET ')

BlogBD = Basededatos('Bloggi.db')



if __name__ == '__main__':
    run()