from flask import render_template, request, redirect
from app.main import main
from app.extensions import db, fl
from app.models import *
from app.forms import *
from flask_login import login_user, login_required

# ******************************************* New Page *******************************************
@ main.route('/')
def index():
    """ This is the index, when you first open the page and are signed in you will be directed 
    here! """
    return render_template("main.html")


# ******************************************* New Page *******************************************
@ main.route('/login', methods=['GET', 'POST'])
def login():
    """ Login page. You will be directed here if you are not logged in.  """
    form = Login(request.form)
    if request.method == 'POST' and form.validate():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        login_user(user)
        redirect('/')
    return render_template("login.html", form=form)
  
  
# ******************************************* New Page *******************************************
@ main.route('/green-house')
@ login_required
def greenhouse():
    """ This is the bulk of the app. A green house monitor and controller this is my favorite 
    page! :) """    
    return render_template("greenhouse.html")


# ******************************************* New Page *******************************************
@ main.route('/calendar')
def calendar():
    """ The calendar page will show events that the gardeners should know about. Like a wedding. I
    do this so the gardeners can prepare and make the garden look spic and span during an event"""
    return render_template("calendar.html")


# ******************************************* New Page *******************************************
@ main.route('/todo-list')
def todo():
    """ Todo: quite self explanitory. It is a todo list for the gardeners so that they know what
    to do. For example:  Clean up Japanese Garden"""
    return render_template("todo.html")