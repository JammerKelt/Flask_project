from flask import Blueprint
from flask import render_template

from mdblog.models import Article

blog = Blueprint("blog", __name__)

@blog.route("/articles/", methods=["GET"])
def view_articles() :
    articles = Article.query.order_by(Article.id.desc())
    return render_template("mod_blog/articles.html", articles=articles)

@blog.route("/articles/<int:art_id>/")
def view_article(art_id):
    article = Article.query.filter_by(id=art_id).first()
    if article:
        return render_template("mod_blog/article.html", article=article)
    return render_template("article_not_found.html", art_id=art_id)
