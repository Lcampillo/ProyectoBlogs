from app import *
from models import Auth
from flask import render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()

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

      message_e = f'''Bienvenido a Bloggi!!\nHola {name}, nos place que empieces a utilizar nuestros servicios de Blog\npara ellos solcitamos
      que actives tu cuenta de usario en el siguiente enlace:\n url=https'''
      #parametros de conexión del correo electronico
      password = "yoyito2020"
      msg['From'] = "profeyoyito2020@gmail.com"
      msg['To'] = email
      msg['Subject'] = "Activación cuenta de usuario"
      # Cuerpo del mensaje se escoje texto plano
      msg.attach(MIMEText(message_e, 'plain'))
      #establecer conexión con el servidor en este caso gmail
      server = smtplib.SMTP('smtp.gmail.com: 587')
      server.starttls()
      #autenticación de las credenciales de correo con el servidor de gmail
      server.login(msg['From'], password)
      #enviar el mensaje a travez del servidor de correo de gmail
      server.sendmail(msg['From'], msg['To'], msg.as_string())
      server.quit()#cerrar la conexión con el servidor

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
