import os
from flask import Flask, render_template, url_for, request, flash, redirect, session
from werkzeug.utils import secure_filename
import sqlite3


db = sqlite3.connect('database/bloggi.db',check_same_thread=False)
cursor = db.cursor()


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/images_posts"
app.secret_key = 'secret'

from controllers.AuthController import *
from controllers.BlogController import *
from controllers.ProfileController import *

if __name__=='__main__':
    app.run(debug=True)