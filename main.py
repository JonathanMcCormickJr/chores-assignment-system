from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)
app.debug = True

# DARK MODE AUTO-ASSIGN

def get_mode():
    

    def is_nighttime():
        new_hampshire_tz = pytz.timezone('America/New_York')
        now = datetime.now(new_hampshire_tz)
        current_time_nh = int(now.strftime("%H%M%S"))
        return not 60000 < current_time_nh < 180000  # Use IRL
        #return 60000 < current_time_nh < 180000  # Use ONLY for testing

    if is_nighttime():
        return 'dark'
    else:
        return 'light'


# Pages

@app.route('/')
def index():
    mode = get_mode()
    return render_template('index.html', mode=mode)

@app.route("/about")
def about():
    mode = get_mode()
    return render_template("about.html", mode=mode)

@app.route("/analytics")
def analytics():
    mode = get_mode()
    return render_template("analytics.html", mode=mode)

@app.route("/survey")
def survey():
    mode = get_mode()
    chores = [
        "Cleaning the kitchen",
        "Vacuuming or sweeping floors",
        "Dusting and cleaning surfaces",
        "Doing laundry",
        "Cleaning bathrooms",
        "Taking out the trash and recycling",
        "Mowing the lawn",
        "Maintaining the garden",
        "Grocery shopping",
        "Cooking and meal preparation",
        "Cleaning windows and mirrors",
        "Organizing and decluttering",
        "Sweeping the porch or walkways",
        "Cleaning the car(s)",
        "Pet care"
    ]
    return render_template('survey.html', mode=mode, chores=chores)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
