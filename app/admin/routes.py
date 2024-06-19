from flask import render_template, request
from flask_login import login_required
from app.extensions import db
from app.models import Todo
from app.admin import admin

# ******************************************* New Page *******************************************
@ admin.route('/test')
def test():
    """ Used to test if everything is working ion the Green house. I think this one will be very
    usefull also it can only be accessed by admins, not the gardeners"""
    return render_template("test.html")


# ******************************************* New Page *******************************************
@ admin.route('/settings')
def settings():
    """ This will be used to alter less main stream things. Like the storm protocol """
    return render_template("settings.html")


# ***************************************** Ajax Request *****************************************
@ admin.route('/todo-list/assignment/<id>/edited', methods=['GET', 'POST'])
@ login_required
def todo_edited(id):
    """ Used for editing a todo item, however this is accessable by super users! """
    if request.method == "POST":
        new_title = request.form['title']
        new_description = request.form['description']
        
    db.session.query(Todo).filter_by(id=id).first()
    print(id, new_title, new_description)
    db.session.commit()
    return 'Done'