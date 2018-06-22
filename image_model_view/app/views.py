from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from .models import Person
"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()


class PersonModelView(ModelView):
    datamodel = SQLAInterface(Person)

    # list_widget = ListThumbnail

    label_columns = {'name':'Name','photo':'Photo','photo_img':'Photo', 'photo_img_thumbnail':'Photo'}
    list_columns = ['photo_img_thumbnail', 'name']
    show_columns = ['photo_img','name']

appbuilder.add_view(PersonModelView, 'Show Person', category="Person")
