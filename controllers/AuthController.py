from app import *
from models import Auth
from flask import render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import choice
import smtplib
from models.Auth import db
import urllib.parse as urlparse
from urllib.parse import parse_qs

msg = MIMEMultipart()

@app.route('/login')
def login():
   return render_template('auth/login.html')

@app.route('/register')
def register():
   return render_template('auth/register.html')

@app.route('/verify', methods=['GET'])
def verify():
   if request.method == 'GET':
          
      parsed = urlparse.urlparse(request.url)     
      email = parse_qs(parsed.query)['email'][0]
      temp_key = parse_qs(parsed.query)['hash'][0]

      return render_template('auth/verify.html', email=email, temp_key=temp_key)
      #for idx, account in enumerate(db):       
      #      if email == account[0] and temp_key == account[2]:
      #             db[idx][3]= True
      #             return redirect(url_for('login'))
      #return redirect(url_for('register'))
   

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
      temp_key = generate_key()

      hazEl = Auth.Auth(name,surname,email,cellphone,password)
      hazEl.set_temp_key(temp_key)

      result = hazEl.register()

      ## Enviar email de activación de cuenta
      message_e = f'''Bienvenido a Bloggi!!

      Hola {name.capitalize()} {surname.capitalize()}.

      Nos place que empieces a utilizar nuestros servicios de Blog, estos son tus datos de acceso:
      
      ----------------------------
      Correo: {email}
      Contraseña: {password}
      ----------------------------

      Por favor, activa tu cuenta presionando el siguiente enlace:
      http://127.0.0.1:5000/verify?email={hazEl.email}&hash={hazEl.activation_key}'''

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

def generate_key():
   longitud = 18
   valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=@#%&+"

   p = ""
   p = p.join([choice(valores) for i in range(longitud)])
   return p
