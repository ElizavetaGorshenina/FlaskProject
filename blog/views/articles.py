from flask import Blueprint, render_template

from blog.models.database import db
from blog.models import Author, Article

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)
