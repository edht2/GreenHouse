from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask('app')
app.config['SECRET_KEY'] = 'the random string'    

@app.route('/')
def index():
  return render_template("form.html", temp=[15,30], rh=[40,70], co2ppm=[100,None])#replace with a db query !!!!!!!!!!!!!!
"""
@app.route('/hd', methods=['GET','POST'])
def handle_data():
  low = request.form['low']
  high = request.form['high']
  difference = high - low
  print(f"LOW:{low} HIGH:{high} DIFF:{difference}")
  return redirect(url_for("index"))
"""
@app.route('/handle_data/<unit>/<min>/<max>/<minDiff>', methods=['POST'])
def formHandle(unit, min, max, minDiff):
    tooFlash = ""
    low = request.form['low']
    high = request.form['high']
    min = int(min)
    max = int(max)
    minDiff = int(minDiff)
    try:
      high = int(high)
      low = int(low)
    except: 
      tooFlash += "Inputs must be a number. "
      return redirect(url_for("index"))
    difference = high - low
    print(f"LOW:{low} HIGH:{high} DIFF:{difference}")
    if difference <= minDiff:
      tooFlash += f"Leave a gap of at least {minDiff} between min and max. "
    
    #elif here for more 
    if low < min or low > max:
      tooFlash += f"Min must be within {min}-{max}{unit}. "
    if high < min+minDiff or high > max+minDiff:
      tooFlash += f"Max must be within {min+minDiff}-{max+minDiff}{unit}. "
    if tooFlash == "": pass#write to db here!!!!!!!!!!!!!!!!!!!!!!!!!
    print(tooFlash)
    if True:flash(tooFlash)
    return redirect(url_for("index"))


app.run(host='0.0.0.0', port=8080)
