from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from flask_appbuilder.charts.views import DirectByChartView
from .models import CountryStats, Country
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

class CountryStatsModelView(ModelView):
    datamodel = SQLAInterface(CountryStats)
    label_columns = {'country': '国家'}
    list_columns = ['stat_date', 'population', 'unemployed_perc', 'poor_perc', 'college']
appbuilder.add_view(CountryStatsModelView, 'Show country stat', category="Statistics")


class CountryModelView(ModelView):
    datamodel = SQLAInterface(Country)
appbuilder.add_view(CountryModelView, 'Show country', category='Statistics')


class CountryDirectChartView(DirectByChartView):
    datamodel = SQLAInterface(CountryStats)
    chart_title = '图表'

    definitions = [
    {
        'label': 'Unemployment',
        'group': 'stat_date',
        'series': ['unemployed_perc', 'college_perc']
    },
    {
        'label': 'Poor',
        'group': 'stat_date',
        'series': ['poor_perc', 'college_perc']
    }
]

db.create_all()

appbuilder.add_view(CountryDirectChartView, 'Show Country Chart', category="Statistics")
