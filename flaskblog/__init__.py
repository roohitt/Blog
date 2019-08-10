from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy# importing all above extensions installed through pip
from flask_login import LoginManager



app = Flask(__name__)   #creating instance a of class flask
 # __name__ is a special varibale in python that is just  the name of the module
#if we run this co de directly in python then __name__ == __main__
#where flask will look for templates and static files
#it is main in our case as we are running in python

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # uri is like url to depict the location of db(which is ///site)/// stands for same loc as the flashblog
db = SQLAlchemy(app) #instance of the database is created
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #login function will be viewed when login required or account is used
login_manager.login_message_category = 'info'


from flaskblog import routes#to avoid circular import