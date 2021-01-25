from flask import render_template, url_for, redirect, render_template_string
from app import mln


@mln.route("/")
@mln.route("/index")
def index():
    return render_template("index.html", title="Models Testing Index")


@mln.route("/models")
def models():
    return render_template("models.html", title="Models Testing Index")
