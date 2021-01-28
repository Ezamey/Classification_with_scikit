from flask import render_template, url_for, redirect, render_template_string
from flask import current_app as app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Models Testing Index")


@app.route("/models")
def models():
    return render_template("models.html", title="Models Testing Index")
