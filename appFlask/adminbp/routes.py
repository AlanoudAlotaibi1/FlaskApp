from flask import Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from appFlask import admin,db ,bcrypt
from appFlask.models import User ,Lesson , Course
adminbp = Blueprint('adminbp',__name__)

class UserModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8)"
        )

    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1


class MyModelView(ModelView): ## for the our models 
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1


class MyAdminIndexView(AdminIndexView):## for the admin and home screans 
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1
    

admin.add_view(UserModelView(User,db.session))
admin.add_view(MyModelView(Lesson,db.session))
admin.add_view(MyModelView(Course,db.session))
