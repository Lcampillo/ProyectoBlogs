from app import *
from flask import render_template

@app.route('/')
def home():
   if "user" in session:
      return render_template('index.html')
   else:
      flash('Inicie sesion para acceder al sistema')
      return redirect(url_for('login'))

@app.route('/post/create')
def createPost():
   if "user" in session:
      return render_template('blog/create.html')
   else:
      flash('Inicie sesion para acceder al sistema')
      return redirect(url_for('login'))

@app.route('/post/single-post')
def singlePost():
   if "user" in session:
      return render_template('blog/single_post.html')
   else:
      flash('Inicie sesion para acceder al sistema')
      return redirect(url_for('login'))