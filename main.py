from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/survey")
def survey():
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
    return render_template('survey.html', chores=chores)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

