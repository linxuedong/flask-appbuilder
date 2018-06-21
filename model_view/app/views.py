from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from .models import ContactGroup, Contact

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

class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)
    label_columns = {'contact_group':'Contact Group'}
    list_columns = ['name', 'address', 'birthday', 'contact_group']

    show_fieldsets = [
        (
            'Summary',
            {'fields': ['name','address','contact_group']}
        ),
        (
            'Persion Info',
            {'fields': ['birthday']}
        )
    ]

class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]

db.create_all()
appbuilder.add_view(GroupModelView,
                    'List Groups',
                    category='Contacts')
appbuilder.add_view(ContactModelView,
                    'List Contact',
                    category='Contacts')
