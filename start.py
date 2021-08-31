from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def start_page():
    return render_template("index.html")


app.run()