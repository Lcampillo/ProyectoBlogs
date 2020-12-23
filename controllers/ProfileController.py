from app import *
from models import Auth
from flask import render_template

@app.route('/profile')
def profile():
   return render_template('profile/edit.html')

@app.route('/update/profile',methods=['GET','POST'])
def updateProfile():
   if request.method == 'POST':
      name = request.form['name']
      surname = request.form['surname']
      cellphone = request.form['cellphone']
      email = request.form['email']
      newPassword = request.form['newPassword']

   hazEl = Auth.Auth(name,surname,email,cellphone,'',newPassword)

   result = hazEl.update()

   if result == 'success':
      flash('Perfil actualizado correctamente')
      return redirect(url_for('profile'))
   else:
      flash('Algo salio mal intentalo nuevamente')
      return redirect(url_for('profile'))