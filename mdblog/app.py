from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.html")

@flask_app.route("/about/")
def view_about():
    return render_template("about.html")

@flask_app.route("/admin/")
def view_admin():
    return render_template("admin.html")

@flask_app.route("/articles/")
def view_articles() :
    return render_template("articles.html")