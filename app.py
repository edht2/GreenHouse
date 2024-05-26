from flask import Flask,  render_template
app = Flask('app')

@app.route('/')
def index():
    return render_template("main.html")
  
@app.route('/green-house')
def greenhouse():
    return render_template("greenhouse.html")
  
@app.route('/calendar')
def calendar():
    return render_template("calendar.html")
  
@app.route('/todo-list')
def todo():
    return render_template("todo.html")
  
@app.route('/test')
def test():
    return render_template("test.html")
  
@app.route('/settings')
def settings():
    return render_template("settings.html")


app.run(host='0.0.0.0', port=8080)