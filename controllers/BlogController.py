from app import *
from flask import render_template

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/post/create')
def createPost():
   return render_template('blog/create.html')

@app.route('/post/single-post')
def singlePost():
   return render_template('blog/single_post.html')