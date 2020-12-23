from app import *
from models import Auth
from flask import render_template

@app.route('/profile')
def profile():
   if "user" in session:
      email = session["user"]
      cursor.execute('SELECT name, surname, contact FROM users WHERE email = ?', (email,))
      result = cursor.fetchone()
      print(result)
      return render_template('profile/edit.html', name=result[0], surname=result[1], contact=result[2], email=email)
   else:
      flash('Inicie sesion para acceder al sistema')
      return redirect(url_for('login'))

@app.route('/update/profile',methods=['GET','POST'])
def updateProfile():
   if "user" in session:
      if request.method == 'POST':
         name = request.form['name']
         surname = request.form['surname']
         cellphone = request.form['cellphone']
         email = request.form['email']
         newPassword = request.form['newPassword']

      hazEl = Auth.Auth(name,surname,email,cellphone,'',newPassword)

      result = hazEl.update()
      print(result)
      if result == 'success':
         flash('Perfil actualizado correctamente')
         return redirect(url_for('profile'))
      else:
         flash('Algo salio mal intentalo nuevamente')
         return redirect(url_for('profile'))
   else:
      flash('Inicie sesion para acceder al sistema')
      return redirect(url_for('login'))