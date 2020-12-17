from app import *
from flask import render_template

@app.route('/profile')
def profile():
   return render_template('profile/edit.html')