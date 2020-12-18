from app import *
from models import Auth
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

      hazEl = Auth.Auth(name,surname,email,cellphone,password)

      result = hazEl.register()

      if result == 'success':
         flash('Dirijase a su correo y active su cuenta para ingresar')
         return redirect(url_for('login'))
      else:
         flash('El correo ya se encuentra registrado')
         return redirect(url_for('register'))

@app.route('/singup', methods=['GET','POST'])
def singup():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']

      hazEl = Auth.Auth('','',email,'',password)

      result = hazEl.login()

      if result == 'true':
         flash('Bienvenido')
         return redirect(url_for('home'))
      else:
         flash('El usuario no existe')
         return redirect(url_for('login'))


