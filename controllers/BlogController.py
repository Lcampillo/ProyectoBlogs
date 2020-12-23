from app import *
from flask import render_template
from models import Blog

@app.route('/')
def home():
   if "user" in session:
      hazEl = Blog.Blog()
      result = hazEl.query()
      return render_template('index.html',posts = result)
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

@app.route('/store/post', methods=['POST','GET'])
def storePost():
   if "user" in session:
      if request.method == 'POST':
         title = request.form['title']
         description = request.form['description']
         published = request.form['published']
         state = request.form['state']

         image = request.files['image']
         filename = secure_filename(image.filename)
         image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

         hazEl = Blog.Blog(title,description,published,state,image)
         result = hazEl.store()

         if result[0] >= 1:
            flash("Post creado correctamente")
            return redirect(url_for('home'))
         else:
            flash("Algo salio mal")
            return redirect(url_for('createPost'))
      else:
         flash("Inicie sesion para acceder al sistema")
         return redirect(url_for('login'))

@app.route('/search', methods=['POST'])
def searchPost():
   if "user" in session:
      if request.method == 'POST':
         title = request.form['title']
      
      hazEl = Blog.Blog(title)

      result = hazEl.search()
      
      if result is not None:
         return render_template('index.html',posts = result)
         
   else:
      flash("Inicie sesion para acceder al sistema")
      return redirect(url_for('login'))
