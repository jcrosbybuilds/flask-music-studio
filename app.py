"""

Name: Jacob Crosby
Date:
Purpose: For Testing

"""


# Import Libraries
from datetime import datetime
from flask import Flask
from flask import render_template



app = Flask(__name__)

@app.route("/")
def home():
    """ Renders the Home page for website """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("home.html", time=current_time)

@app.route("/about")
def about():
    """ Renders the About page for website """
    return render_template("about.html")

@app.route("/contact")
def contact():
    """ Renders the Contact page for the website"""
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()
