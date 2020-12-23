from app import *
from models import Auth
from flask import render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from models.Auth import db
import urllib.parse as urlparse
from urllib.parse import parse_qs

msg = MIMEMultipart()

@app.route('/login')
def login():
      return render_template('auth/login.html')

@app.route('/logout')
def logout():
      session.pop("user",None)
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

      print(parsed,email,temp_key,'\n')

      cursor.execute("UPDATE users SET activated = 'true' WHERE email = ? AND hash = ?",(email,temp_key))
      db.commit()

      cursor.execute("SELECT * FROM users WHERE email = ? ", (email,))
      result = cursor.fetchone()

      if email == result[6]:
         return render_template('auth/verify.html', email=email, temp_key=temp_key)
      else:
         flash('Algo salio mal')
         return redirect(url_for('register'))
 

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

      if result[0] >= 1:
         ## Enviar email de activación de cuenta
         message_e = f"""Bienvenido a Bloggi!!

         Hola {name.capitalize()} {surname.capitalize()}.

         Nos place que empieces a utilizar nuestros servicios de Blog, estos son tus datos de acceso:

         ----------------------------
         Correo: {email}
         Contraseña: {password}
         ----------------------------

         Por favor, activa tu cuenta presionando el siguiente enlace:
         http://127.0.0.1:5000/verify?email={email}&hash={result[3]}"""

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

         flash('Dirijase a su correo y active su cuenta para ingresar')
         return redirect(url_for('login'))
      else:
         flash('Algo salio mal intentalo nuevamente')
         return redirect(url_for('register'))

@app.route('/singup', methods=['GET','POST'])

def singup():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']

      hazEl = Auth.Auth('','',email,'',password)

      login = hazEl.login()

      print(login,'\n',email)

      # Si existe el usuario y contraseña:
      try:
         if login[6] == email and login[7] == 'true':
            session["user"] = email
            session["id"] = login[0]
            flash(f"Bienvenido {login[2]}")
            return redirect(url_for('home'))
         elif login[7] == 'false':
            flash('El usuario no ha sido activado')
            return redirect(url_for('login'))
      except:
         flash('Datos de inicio inválidos, por favor intente nuevamente')
         return redirect(url_for('login'))