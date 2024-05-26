from flask import render_template
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