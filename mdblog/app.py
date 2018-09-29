from flask import Flask
from flask import render_template

from .database import articles

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
    return render_template("articles.html", articles=articles.items())

@flask_app.route("/articles/<int:art_id>")
def view_article(art_id):
    article = articles.get(art_id)
    if article:
        return render_template("article.html", article=article)
    return render_template("article_not_found.html", art_id=art_id)