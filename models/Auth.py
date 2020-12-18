db = []

class Auth():

    def __init__(self, name = None, surname = None, email= None, contact = None, password = None, newPassword = None):
        self.name = name
        self.surname = surname
        self.email = email
        self.contact = contact
        self.password = password
        self.newPassword = newPassword
    def login(self):
        for account in db:       
            if self.email in account[0]:
                return 'true'

    def register(self):
        for account in db:       
            if self.email in account[0]:
               return 'danger' 
        account = (self.email,self.password)
        db.append(account)
        return 'success'


    def update(self):
        for idx, account  in enumerate(db):       
            if self.email in account[0]:
                account = (self.email,self.newPassword)
                db[idx] = account
                return 'success'
