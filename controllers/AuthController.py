from app import *
from flask import render_template

@app.route('/login')
def login():
   return render_template('auth/login.html')

@app.route('/register')
def register():
   return render_template('auth/register.html')

@app.route('/recuperar_contraseña')
def recover():
   return render_template('auth/recover.html')

@app.route('/store', methods=['GET','POST'])
def store():
   if request.method == 'POST':
      name = request.form['name']
      surname = request.form['surname']
      email = request.form['email']
      cellphone = request.form['cellphone']
      password = request.form['password']

      return f"{name} {surname} {email} {cellphone} {password}"
