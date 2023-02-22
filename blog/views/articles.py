from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.views.users import USERS


articles_app = Blueprint("articles_app", __name__)
ARTICLES = {
    1: {"title": "Flask",
        "text": "Micro web framework written in Python.",
        "user": 3},
    2: {"title": "Django",
        "text": "Free and open-source, Python-based web framework that follows the model–template–views (MTV) "
                "architectural pattern.",
        "user": 1},
    3: {"title": "JSON:API",
        "text": "JSON (JavaScript Object Notation) API is an application programming interface designed for "
                "lightweight data interchange.",
        "user": 2}
}


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id: int):
    try:
        article_title = ARTICLES[article_id]['title']
        article_text = ARTICLES[article_id]['text']
        article_user = ARTICLES[article_id]['user']
        article_user_name = USERS[article_user]
    except KeyError:
        raise NotFound(f"Article #{article_id} doesn't exist!")
    return render_template('articles/details.html', article_id=article_id, article_title=article_title, article_text=article_text, article_user=article_user, article_user_name=article_user_name)
