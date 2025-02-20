from json import dumps
from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required
from datetime import date as dt_date
from datetime import timedelta, datetime
from app.main import main
from app.extensions import db
from app.models import *
from app.forms import Login, Env_limits

# ******************************************** Index *********************************************
""" This is the index, when you first open the website and are signed in you will be directed 
    here! """
@ main.route('/')
@ login_required
def index():
    return render_template("main.html")


# ******************************************** Login *********************************************
""" Login page. You will be redirected here if you are not logged in.  """
@ main.route('/login', methods=['GET', 'POST'])
def login():
    form = Login(request.form)
    # create a form object
    if request.method == 'POST' and form.validate():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        login_user(user, remember=True)
        # I sign in the user
        # NOTE: I have already validated their usernames with the password!
        return redirect("/")
    return render_template("login.html", form=form)
  
  


# ****************************************** GreenHouse ******************************************
""" This is the bulk of the app. A green house monitor and controller, this is my favorite 
    page! :) """
@main.route("/greenhouse", methods=["GET", "POST"])
@ login_required
def greenhouse():
    latest_env_limits_record = vars(EnvLimits.query.order_by(EnvLimits.date_time.desc()).first())  # dictionary of all records
    form = Env_limits(latest_env_limits_record, request.form)
    env_limits = vars(EnvLimits.query.order_by(EnvLimits.date_time.desc()).first())  # dictionary of all records
    return render_template("greenhouse.html", form=form)


# ****************************************** GreenHouse/actual ***********************************

@main.route("/greenhouse_ajax", methods=['GET'])
@ login_required
def greenhouse_actual():
    czvars = "temp rh".split(" ")#["temp","rh"]
    """   
    live_sensor_readings ={
                           'cz1_temp': 15, 
                           'cz1_rh': 75, 

                           'cz1_bed1': 55, 
                           'cz1_bed2': 56,
                           'cz1_bed3': 55, 

                           'cz2_temp': 17, 
                           'cz2_rh': 75, 

                           'cz2_bed4': 54, 
                           'cz2_bed5': 56,
                           'cz2_bed6': 55,
                           'cz2_bed7': 55,
                           'cz2_bed8': 55
                           }

        live_sensor_readings = {}
    for cz_no in [0,1]:
        cz = ClimateZone.query.get(cz_no+1)
        live_sensor_readings[f"cz{cz_no+1}_temp"] = cz.temp
        live_sensor_readings[f"cz{cz_no+1}_rh"] = cz.rh

        if cz_no == 0: beds = Bed.query.all()[5:]
        else: beds = Bed.query.all()[:5]
        
        clock = 0
        if cz_no == 1:clock = 3
        for bed in beds:
            clock += 1
            live_sensor_readings[f"cz{cz_no+1}_bed{clock}"] = bed.sm_percent

    """
    live_sensor_readings = {}# json starter
    no_of_beds = 8# TODO add to a config oneday
    beds_to_find = [i+1 for i in range(no_of_beds)]# makes a list starting at 1 not 0
    beds = []
    for bed in beds_to_find:

        bed_latest_record = Bed.query.filter( # searches for the most reacent record for each bed
                Bed.bed_name.like(
                    f"%bed{bed}%"
                )
        ).order_by(
            Bed.id.desc()
        ).first()

        if bed_latest_record: # adds ans to query
            beds.append(bed_latest_record)
        else: # if there is no result, say NoDat
            beds.append("NoDat")

    for cz_no in [0,1]: # runs all code for both czs
        cz = ClimateZone.query.get(cz_no+1) # gets the current climate zone obj from db
        live_sensor_readings[f"cz{cz_no+1}_temp"] = cz.temp # adds temp to json
        live_sensor_readings[f"cz{cz_no+1}_rh"] = cz.rh # adds rh to json
        counter = 0
        if cz_no == 1:counter = 3 # TODO:add config, how many are in cz1
        for bed in beds: 
            counter += 1
            live_sensor_readings[f"cz{cz_no+1}_bed{counter}"] = bed.sm_percent #adds to dict

    json_str = dumps(live_sensor_readings)# jsonify the dict
    return str(json_str) # send that shit, i mean poo

# ******************************************* Calendar *******************************************
""" The calendar page will show events that the gardeners should know about. Like a wedding. I
    do this so the gardeners can prepare and make the garden look spic and span during an event"""
@ main.route('/calendar/display/<week>')
@ login_required
def calendar(week):
    try:
        DAYS = "Mon Tue Wed Thu Fri Sat Sun".split()
        upcoming_events = []
        pd = dt_date.today()
        pd += timedelta(days=7*int(week)-pd.weekday())
        
        for day in range(7):
            # so for every day in a seven-day period
            nd = pd+timedelta(days=day)
            events_for_ths_day = db.session.query(Event).filter_by(date=nd).all()
            upcoming_events.append([nd.strftime('%d/%m/%Y')]+events_for_ths_day)
        
        return render_template("calendar.html", dates=upcoming_events, len_dates=len(upcoming_events), dn=DAYS)
    except:
        return redirect(url_for("main.calendar", week=0))


# *************************************** Calendar Navbar ****************************************
""" On the calendar page there are two buttons, these buttons redirect the user to another redirect
    but with the specified week ofset!"""
@ main.route('/calendar/display/<week>/<act>')
@ login_required
def calendar_navbar(week, act):
    try:
        if act == 'next':
            return redirect(url_for("main.calendar", week=str(int(week)+1)))
        if act == 'prev':
            return redirect(url_for("main.calendar", week=str(int(week)-1)))
        # These two conditionals help move users between pages (weeks)
    except:
        return redirect(url_for("main.calendar", week=0))
        # And of course, we must add a conditional to stop errno 500! (Internal Server Error)
    

# ****************************************** New date ********************************************
""" I have this page so events, meetings etc. can be added. This is available to every user
    regardless of their permissions. """
@ main.route('/calendar/add/<day>/<month>/<year>/<title>')
@ login_required
def add_date(year, month, day, title):
    try:
        date = dt_date(int(year), int(month), int(day))
        new_event = Event(date=date, event_title=title)
        # create the new db record!
        db.session.add(new_event)
        db.session.commit()
        # save it to the db
        return redirect(url_for("main.calendar", week=0))
    except:
        return redirect(url_for("main.calendar", week=0))
        # And of course, we must add a conditional to stop errno 500! (Internal Server Error)
    
 
# ****************************************** Calendar fix ****************************************
""" If the user tries to go to '/calendar' I do not allow them as I need to know what week you want
    to retrive. To fix them I redirect the user to the present week! """
@ main.route('/calendar')
@ login_required
def calendar_redirect():
    return redirect(url_for("main.calendar", week=0))
    
    
# ********************************************* Todo *********************************************
""" Todo: quite self explanitory. It is a todo list for the gardeners so that they know what
    to do. For example:  Clean up Japanese Garden"""
@ main.route('/todo-list')
@ login_required
def todo():
    tasks = db.session.query(Todo).filter_by(is_completed=False).all()
    return render_template("todo.html", tasks=tasks, tasks_len=len(tasks))
    # I retrive all of the records and return them, simple as that!


# ****************************************** Assignment *******************************************
""" Gives a detailed description of what and where the assignment holds """
@ main.route('/todo-list/assignment/<id>')
@ login_required
def todo_assignment(id):
    try:
        task = db.session.query(Todo).filter_by(id=id).first()
        #img = url_for('../static/img/todo/' + task.image_directory)
        return render_template("todo_assignment.html", task=task)
        # I return the requested task, again very simple :)
    except:
        return redirect('todo-list')
        # I have a try statment in the event the user messed up the URL. I don't want the user to
        # see an error message, so I just redirect them back to the todo list


# ************************************* Check Off Assignment *************************************
""" Marks a todo item as done! simple as that! """
@ main.route('/todo-list/assignment/<id>/completed')
@ login_required
def todo_completed(id):
    try:
        db.session.query(Todo).filter_by(id=id).first().completed()
        # the Todo.completed method checks off the assignment!
        db.session.commit()
        return 'Done'
    except:
        redirect('todo-list/assignment')