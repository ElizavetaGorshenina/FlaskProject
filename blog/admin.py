from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from blog import models
from blog.models.database import db


admin = Admin(name="Blog Admin", template_mode="bootstrap4")
