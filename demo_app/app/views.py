from flask import render_template, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, SimpleFormView
from app import appbuilder, db
from flask_appbuilder import AppBuilder, expose, BaseView, has_access
from . import forms
from flask_babel import lazy_gettext as _

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

class MyView(BaseView):
    route_base = "/myview"

    @expose('/method1/<string:name>')
    def method1(self, name):
        return self.render_template('method1.html', name=name)

    @expose('/method2/<string:name>')
    def method2(self, name):
        welcome = 'Hello, ' + name
        return welcome

appbuilder.add_view_no_menu(MyView())

class SimpleView(BaseView):
    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        return 'Hello, World!'

    @expose('/method2/<string:name>')
    @has_access
    def method2(self, name):
        return 'Hello, ' + name

appbuilder.add_view(SimpleView, "method1", category='My View')
appbuilder.add_link("method2", href="/simpleview/method2/john", category='My View')


class MyFormView(SimpleFormView):
    form = forms.MyForm
    form_title = 'This is my first view'
    message = 'My form submitted'

    def form_get(self, form):
        form.field1.data = 'This was prefilled'

    def form_post(self, form):
        flash(self.message, 'info')

appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
                     category="My Forms", category_icon="fa-cogs")
