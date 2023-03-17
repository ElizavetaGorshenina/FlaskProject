from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetail
from blog.api.article import ArticleList, ArticleDetail
from blog.api.author import AuthorList, AuthorDetail
from blog.api.user import UserList, UserDetail


def init_api(app):
    api = Api(app)
    api.route(TagList, "tag_list", "/api/tags/")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/")
    api.route(ArticleList, "article_list", "/api/articles/")
    api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>/")
    api.route(AuthorList, "author_list", "/api/authors/")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>/")
    api.route(UserList, "user_list", "/api/users/")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/")
    return api
