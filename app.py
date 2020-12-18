from flask import Flask, render_template, url_for, request
import sqlite3

db = sqlite3.connect('bloggi.db')

cursor = db.cursor()

app = Flask(__name__)

from controllers.AuthController import *
from controllers.BlogController import *
from controllers.ProfileController import *

if __name__=='__main__':
    app.run(debug=True)