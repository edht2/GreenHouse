from json import dumps
from flask import render_template, request, redirect, url_for, jsonify
from datetime import date as dt_date
from datetime import timedelta, datetime
from app.main import main
from app.extensions import db
from app.models import *
from app.forms import Login, Env_limits
from app.auth import token_required #import from auth.py
from flask import current_app

# ******************************************** Index *********************************************
""" This is the index, when you first open the website and are signed in you will be directed 
    here! """
@ main.route('/')
def index():
    return render_template("main.html")


# ******************************************** Login *********************************************
""" Login page. You will be redirected here if you are not logged in.  """
main.route('/login', methods=['GET', 'POST'])
def login():
    form = Login(request.form)
    if request.method == 'POST' and form.validate():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        return redirect("/") #removed login_user
    return render_template("login.html", form=form)
  
  


# ****************************************** GreenHouse ******************************************
""" This is the bulk of the app. A green house monitor and controller, this is my favorite 
    page! :) """
@main.route("/greenhouse", methods=["GET", "POST"])
def greenhouse():
    latest_env_limits_record = vars(EnvLimits.query.order_by(EnvLimits.date_time.desc()).first())  # dictionary of all records
    form = Env_limits(latest_env_limits_record, request.form)
    env_limits = vars(EnvLimits.query.order_by(EnvLimits.date_time.desc()).first())  # dictionary of all records
    return render_template("greenhouse.html", form=form)


# ****************************************** GreenHouse/actual ***********************************

@main.route("/greenhouse_ajax", methods=['GET'])
def greenhouse_actual():
    live_sensor_readings = {} # json starter
    no_of_beds = current_app.config.get('BED_NUM', 8) # go to config.py for hardcoded bed numbers.
    cz1_bed_num = current_app.config.get('NO_OF_BEDS_IN_CZ1', 3)
    beds_to_find = [i+1 for i in range(no_of_beds)]# makes a list starting at 1 not 0
    beds = []
    for bed_index in beds_to_find:
        bed_latest_record = Bed.query.filter( # searches for the most recent record for each bed
                Bed.bed_name.like(
                    f"%bed{bed_index}%"
                )
        ).order_by(
            Bed.id.desc()
        ).first()

        beds.append(bed_latest_record) # Append the Bed object (or None if not found)

    for cz_no in [0,1]: # runs all code for both czs
        cz = ClimateZone.query.get(cz_no+1) # gets the current climate zone obj from db
        if cz:
            live_sensor_readings[f"cz{cz_no+1}_temp"] = cz.temp # adds temp to json
            live_sensor_readings[f"cz{cz_no+1}_rh"] = cz.rh # adds rh to json
            live_sensor_readings[f"cz{cz_no+1}_VPD"] = cz.VPD # adds rh to json
            counter = 0
            start_bed = 1 if cz_no == 0 else cz1_bed_num
            
            for i in range(cz1_bed_num if cz_no == 0 else (no_of_beds - cz1_bed_num)):
                bed = beds[start_bed + i -1] # Adjust index to match beds list
                live_sensor_readings[f"cz{cz_no+1}_bed{start_bed + i}"] = bed.sm_percent if isinstance(bed, Bed) else None
        else:
            live_sensor_readings[f"cz{cz_no+1}_temp"] = None
            live_sensor_readings[f"cz{cz_no+1}_rh"] = None
            live_sensor_readings[f"cz{cz_no+1}_VPD"] = None
            for i in range(no_of_beds):
                live_sensor_readings[f"cz{cz_no+1}_bed{i+1}"] = None

    return jsonify(live_sensor_readings)

# ******************************************* Calendar *******************************************
""" The calendar page will show events that the gardeners should know about. Like a wedding. I
    do this so the gardeners can prepare and make the garden look spic and span during an event"""
@ main.route('/calendar/display/<week>')
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
def calendar_redirect():
    return redirect(url_for("main.calendar", week=0))
    
    
# ********************************************* Todo *********************************************
""" Todo: quite self explanitory. It is a todo list for the gardeners so that they know what
    to do. For example:  Clean up Japanese Garden"""
@ main.route('/todo-list')
def todo():
    tasks = db.session.query(Todo).filter_by(is_completed=False).all()
    return render_template("todo.html", tasks=tasks, tasks_len=len(tasks))
    # I retrive all of the records and return them, simple as that!


# ****************************************** Assignment *******************************************
""" Gives a detailed description of what and where the assignment holds """
@ main.route('/todo-list/assignment/<id>')
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
def todo_completed(id):
    try:
        db.session.query(Todo).filter_by(id=id).first().completed()
        # the Todo.completed method checks off the assignment!
        db.session.commit()
        return 'Done'
    except:
        redirect('todo-list/assignment')