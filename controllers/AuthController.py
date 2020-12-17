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